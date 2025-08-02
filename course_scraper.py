from data import BASE_URL, ENDPOINTS, TERM_DATE_VALUES, CRSE_UNSC_VALUES
from utils.meeting_days import MeetingDays
from utils.course_type import CourseType
from bs4 import BeautifulSoup
from course import Course
import requests
import re

class CourseScraper:
    def __init__(self, term):
        self.session = requests.Session()
        self.term = term

    def _fetch_valid_subjects(self, soup):
        select = soup.find("select", {"name" : "sel_subj"})
        subjects = select.find_all("option")

        # gets all valid course subjects directly from patriot web
        valid_subjects = set()
        for subject in subjects:
            value = subject.get("value")
            if value and value != "dummy":
                valid_subjects.add(value)

        return valid_subjects

    # returns the soup of the 2nd page, where you're inputting all the information of the class.
    def _get_term_date_soup(self, soup):
        form = soup.find("form")
        hidden_inputs = form.find_all("input", type='hidden')
        data = {input.get("name"): input.get("value") for input in hidden_inputs}
        data["p_term"] = self.term

        post_url = f"{BASE_URL}{ENDPOINTS['term_date']}"
        post_response = self.session.post(post_url, data=data)
        return BeautifulSoup(post_response.text, "html.parser")
    
    # returns the soup of the 3rd page of all the courses under a subject.
    def _get_crse_unsec_soup(self, soup, subject):
        valid_subjects = self._fetch_valid_subjects(soup) # list of all valid course subjects
        if subject not in valid_subjects:
            print(f"{subject} is not a valid subject!")
            return None

        # CRSE_UNSC_VALUES holds all the valid default data for the form.
        # Just one thing needs to be changed, that being the sel_subject input
        data = CRSE_UNSC_VALUES
        data["term_in"] = self.term
        data["sel_subj"][1] = subject

        post_url = f"{BASE_URL}{ENDPOINTS['crse_unsec']}"
    
        post_response = self.session.post(post_url, data=data)

        return BeautifulSoup(post_response.text, "html.parser")
    
    # scrapes from the initial term select page to the page containing all courses in a certain subject. returns that soup
    def _get_courses_page(self, subject):
        url = f"{BASE_URL}{ENDPOINTS['dyn_sched']}"

        response = None

        # raises an exception if the status code is not 200.
        try:
            response = self.session.get(url, timeout=5)
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            print(f"HTTP Error: {e}")
        except requests.exceptions.RequestException as e:
            print(f"Request Error: {e}")

        soup = BeautifulSoup(response.text, "html.parser") # gets the soup for the initial URL.
        soup = self._get_term_date_soup(soup) # fills out form on initial page with valid data, posts to course search page. returns the soup for that page.
        soup = self._get_crse_unsec_soup(soup, subject) # fills out form for course serach page with valid data, posts to course listings, and return a soup.

        return soup # this soup represents
    
    # returns the 3 tr elements in a course listing as html
    def get_listing_soup(self, subject, target_number, target_section):
        soup = self._get_courses_page(subject)
        if soup is None:
            return None

        table = soup.find("table", {"class" : "datadisplaytable"})
        #rows = table.find_all("th", class_="ddtitle") # only html rows with class ddtitle contain the relevant information for extracting the CRN

        rows = [
            tr for tr in table.find_all("tr")
            if tr.find_parent("tr") is None
        ]
        
        for i, row in enumerate(rows[::3]):
            listing = row.find("a")
            listing_text = listing.get_text(strip=True)
            #print(listing_text)

            # converts something like this: "Precalculus Mathematics - 71565 - MATH 105 - 001"
            # into this: ["Precalculus Mathematics", "71565", "MATH 105", "001"]
            parts = listing_text.split(" - ") 

            if len(parts) >= 4: # in case the course name has a dash in it
                course_code = parts[-2] # e.g., "MATH 125"
                course_number = course_code.split()[-1] # extracts the number from course_code. e.g., "Math 125" -> "125"
                course_section = parts[-1]

                # returns the CRN if the target number and course section are found
                if course_number == target_number and course_section == target_section:
                    #print(listing_text)
                    #new_html = str(rows[i*3]) + str(rows[(i*3) + 1]) + str(rows[(i*3) + 2])
                    new_html = ''.join(str(tag) for tag in rows[i*3:i*3 + 3])
                    return BeautifulSoup(new_html, "html.parser")
        #'''
        return None

    # returns a course object with its information populated by the html returned by get_listing()
    def get_course(self, subject, target_number, target_section):
        soup = self.get_listing_soup(subject, target_number, target_section)
        if soup is None:
            return None

        heading_th = soup.find("th", class_={"ddtitle"})
        heading = heading_th.find('a')

        # converts heading from something like this: "Precalculus Mathematics - 71565 - MATH 105 - 001"
        # into this: ["Precalculus Mathematics", "71565", "MATH 105", "001"]
        parts = heading.text.split(" - ")
        crn = parts[-3] # the CRN is guaranteed to be the 3rd last item in the list

        url = f"{BASE_URL}{ENDPOINTS['detail_sched']}?term_in={self.term}&crn_in={crn}"
        course_code = parts[-2] # the CRN is guaranteed to be the 2nd last item in parts
        section = parts[-1] # the CRN is guaranteed to be the last item in parts
        class_name = ' - '.join(parts[:-3]) # .split separates on " - ", so in case that was part of the course title itself, it'll be restored

        table = soup.find("table", {"class" : "datadisplaytable"})
        cols = soup.find_all("td")[2:]

        instructor = cols[6].text
        time_period = cols[4].text
        meeting_days = cols[2].text
        class_type = cols[5].text
        location = cols[3].text
        return Course(url, course_code, section, class_name, instructor, location, time_period, meeting_days, class_type)
