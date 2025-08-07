from bs4 import BeautifulSoup
from data import BASE_URL, ENDPOINTS
from course import Course
from course_email import CourseEmail
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

    # Sends an email for when a course is available. Returns true if email is sent, false if the email sending
    # failed or course isn't available
    def send_availability_email(self, mail: CourseEmail):
        # this method will return false if the course is not available
        if not self.course.is_class_available():
            return False

        email_subject = f"{self.course.course_code} is NOW AVAILABLE!"
        email_body = (
            f"{self.course.course_code}, taught by Prof. {self.course.instructor}, is available!\n"
            f"Log in to PatriotWeb now to claim your seat!\n\n"
            f"Current capacities: {self.course.seats_taken}/{self.course.capacity} seats taken | "
            f"{self.course.waitlist_seats_taken}/{self.course.waitlist_capacity} waitlist seats taken"
        )

        # send email
        return mail.send_email(email_subject, email_body)

    def send_unavailability_email(self, mail:CourseEmail):
        # this method will return false if the course is available
        if self.course.is_class_available():
            return False

        email_subject = f"{self.course.course_code} is no longer available"
        email_body = f"{self.course.course_code}, taught by Prof. {self.course.instructor}, is no longer available.\n"
        if self.course.waitlist_capacity == 0:
            email_body += f"There is no waitlist available for this class.\n\n"
        else:
            if self.course.waitlist_seats_taken == 1:
                email_body += f"There is currently 1 person on the waitlist.\n\n"
            else:
                email_body += f"There are currently {self.course.waitlist_seats_taken} people on the waitlist.\n\n"
        email_body += f"{self.course.waitlist_seats_taken}/{self.course.waitlist_capacity} waitlist seats taken."

        return mail.send_email(email_subject, email_body)


    def __str__(self):
        return (
            f"{self.course}\n"
            f"Seats Available: {self.course.remaining_seats} / {self.course.capacity}\n"
            f"Waitlist Available: {self.course.waitlist_remaining} / {self.course.waitlist_capacity}"
        )