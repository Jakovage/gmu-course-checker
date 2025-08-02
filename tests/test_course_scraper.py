# import unit testing
import unittest

# import statements to access classes from other files
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from course_scraper import CourseScraper
from course import Course

# import data from testing_data.py
from tests.testing_data import FALL_2025_VALUE, FALL_2025_COURSES

class TestCourseScraper(unittest.TestCase):
    # code to run before every test
    def setUp(self):
        # set up the scraper function
        self.scraper = CourseScraper(FALL_2025_VALUE)

        # set up indecies for FALL_2025_COURSES
        self.CS_112_001 = 0
        self.CS_262_004 = 1
        self.MATH_203_DL1 = 2
        self.MATH_125_DL2 = 3
        self.INVALID_DATA = 4

        # create course objects
        self.cs_112_001 = self.scraper.get_course(*FALL_2025_COURSES[self.CS_112_001])
        self.cs_262_004 = self.scraper.get_course(*FALL_2025_COURSES[self.CS_262_004])
        self.math_203_dl1 = self.scraper.get_course(*FALL_2025_COURSES[self.MATH_203_DL1])
        self.math_125_dl2 = self.scraper.get_course(*FALL_2025_COURSES[self.MATH_125_DL2])

    # code to run after every test
    def tearDown(self):
        pass

    # test Course object creation
    def test_valid_course_object_creation(self):
        self.assertIsNotNone(self.cs_112_001)
        self.assertIsNotNone(self.cs_262_004)
        self.assertIsNotNone(self.math_203_dl1)
        self.assertIsNotNone(self.math_125_dl2)

    # test invalid data for Course object creation
    def test_invalid_course_object_creation(self):
        self.assertIsNone(self.scraper.get_course(*FALL_2025_COURSES[self.INVALID_DATA]))

    # test course infomation
    def test_course_info_scrape(self):
        # CS 112 Section 001 Fall 2025
        self.assertEqual(self.cs_112_001.course_code, "CS 112")
        self.assertEqual(self.cs_112_001.section, "001")
        self.assertEqual(self.cs_112_001.class_name, "Intro Computer Programming")
        self.assertEqual(self.cs_112_001.instructor, "Ghada Adam  Abdelmoumin (P)")
        self.assertEqual(self.cs_112_001.location, "Enterprise Hall 178")
        self.assertEqual(self.cs_112_001.time_period, "Aug 25, 2025 - Dec 17, 2025")

        # MATH 203 Section DL1 Fall 2025
        self.assertEqual(self.math_203_dl1.course_code, "MATH 203")
        self.assertEqual(self.math_203_dl1.section, "DL1")
        self.assertEqual(self.math_203_dl1.class_name, "Linear Algebra")
        self.assertEqual(self.math_203_dl1.instructor, "Sarah T  Khankan (P)")
        self.assertEqual(self.math_203_dl1.location, "ON LINE")
        self.assertEqual(self.math_203_dl1.time_period, "Aug 25, 2025 - Dec 17, 2025")

    # test MeetingDays Info
    def test_meeting_days(self):
        # check meeting days for CS 112-001
        self.assertFalse(self.cs_112_001.meeting_days.is_async_section)
        self.assertEqual(self.cs_112_001.meeting_days.meeting_days["Monday"], True)
        self.assertEqual(self.cs_112_001.meeting_days.meeting_days["Tuesday"], False)
        self.assertEqual(self.cs_112_001.meeting_days.meeting_days["Wednesday"], True)
        self.assertEqual(self.cs_112_001.meeting_days.meeting_days["Thursday"], False)
        self.assertEqual(self.cs_112_001.meeting_days.meeting_days["Friday"], False)
        self.assertEqual(self.cs_112_001.meeting_days.meeting_days["Saturday"], False)
        self.assertEqual(self.cs_112_001.meeting_days.meeting_days["Sunday"], False)

        # check meeting days for MATH 125-DL2
        self.assertTrue(self.math_125_dl2.meeting_days.is_async_section)
        self.assertEqual(self.math_125_dl2.meeting_days.meeting_days["Monday"], False)
        self.assertEqual(self.math_125_dl2.meeting_days.meeting_days["Tuesday"], False)
        self.assertEqual(self.math_125_dl2.meeting_days.meeting_days["Wednesday"], False)
        self.assertEqual(self.math_125_dl2.meeting_days.meeting_days["Thursday"], False)
        self.assertEqual(self.math_125_dl2.meeting_days.meeting_days["Friday"], False)
        self.assertEqual(self.math_125_dl2.meeting_days.meeting_days["Saturday"], False)
        self.assertEqual(self.math_125_dl2.meeting_days.meeting_days["Sunday"], False)
    
if __name__ == "__main__":
    unittest.main()

