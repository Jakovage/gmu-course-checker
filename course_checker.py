from bs4 import BeautifulSoup
from data import BASE_URL, ENDPOINTS
from course import Course
import requests

class CourseChecker:
    def __init__(self, course: Course):
        self.course = course
        self.update()

    def _get_course_soup(self):
        url = f"{self.course.url}"

        response = None

        # raises an exception if the status code is not 200.
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            print(f"HTTP Error: {e}")
        except requests.exceptions.RequestException as e:
            print(f"Request Error: {e}")

        return BeautifulSoup(response.text, "html.parser") # gets the soup for the initial URL.
    
    def update(self):
        soup = self._get_course_soup()
        capacities = soup.find_all("td", attrs={"class" : "dddefault"})
        capacity = int(capacities[1].text)
        remaining_seats = int(capacities[3].text)
        waitlist_capacity = int(capacities[4].text)
        waitlist_remaining = int(capacities[6].text)

        self.course.update_seat_info(capacity, remaining_seats, waitlist_capacity, waitlist_remaining)

    def __str__(self):
        return (
            f"{self.course}\n"
            f"Seats Available: {self.course.remaining_seats} / {self.course.capacity}\n"
            f"Waitlist Available: {self.course.waitlist_remaining} / {self.course.waitlist_capacity}"
        )