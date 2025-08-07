# import unit testing
import unittest

# import os module to access .env file data
from dotenv import load_dotenv

# import statements to access other classes
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# import other classes
from course_email import CourseEmail
from course_scraper import CourseScraper
from course_checker import CourseChecker

# import testing data
from testing_data import FALL_2025_AVAIL_COURSES
from testing_data import FALL_2025_UNAVAIL_COURSES
from testing_data import FALL_2025_VALUE

class TestCourseChecker(unittest.TestCase):
    # load environment variables
    load_dotenv()

    def setUp(self):
        self.mail = CourseEmail(os.getenv("TEST_RECIPIENT_2"))
        self.scraper = CourseScraper(FALL_2025_VALUE)

    def test_course_availability_email(self):
        fall_25_open_courses = []
        for course_data in FALL_2025_AVAIL_COURSES:
            course = self.scraper.get_course(*course_data)
            fall_25_open_courses.append(course)

        course_checkers = []
        for course in fall_25_open_courses:
            course_checkers.append(CourseChecker(course))

        for checker in course_checkers:
            self.assertTrue(checker.send_availability_email(self.mail))

    def test_course_unavailability_email(self):
        fall_25_closed_courses = []
        for course_data in FALL_2025_UNAVAIL_COURSES:
            course = self.scraper.get_course(*course_data)
            fall_25_closed_courses.append(course)

        course_checkers = []
        for course in fall_25_closed_courses:
            course_checkers.append(CourseChecker(course))

        for checker in course_checkers:
            self.assertTrue(checker.send_unavailability_email(self.mail))



if __name__ == '__main__':
    unittest.main()
