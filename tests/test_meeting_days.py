# import unit testing module
import unittest

# import statement to access contents from other files
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.meeting_days import MeetingDays

# import data from testing_day.py
from tests.testing_data import SINGLE_DAY_STRINGS
from tests.testing_data import MULTI_DAY_STRINGS
from tests.testing_data import WHITESPACE_STRINGS
from tests.testing_data import SINGLE_DAY_DICT_CORRECT
from tests.testing_data import MULTI_DAY_DICT_CORRECT
from tests.testing_data import NO_MEETING_DAYS_DICT

class TestCourseScraper(unittest.TestCase):

    # tests input strings representing single meeting days
    def test_single_day_strings(self):
        i = 0
        for days_string in SINGLE_DAY_STRINGS:
            days = MeetingDays(days_string)

            # compare generated meeting_days dict to a dict with correct values
            self.assertDictEqual(days.meeting_days, SINGLE_DAY_DICT_CORRECT[i])

            # check that the is_async_section flag is false
            self.assertFalse(days.is_async_section)

            # increment index
            i = i + 1

    # tests input strings representing multiple meeting days
    def test_multi_day_strings(self):
        i = 0
        for days_string in MULTI_DAY_STRINGS:
            days = MeetingDays(days_string)

            # compare generated meeting days dict to a dict with correct values
            self.assertDictEqual(days.meeting_days, MULTI_DAY_DICT_CORRECT[i])

            # check that the is_async_section flag is false
            self.assertFalse(days.is_async_section)

            # increment index
            i = i + 1

    # test input strings representing whitspace strings, which represent
    # asyncronous sections
    def test_whitespace_strings(self):
        for whitespace in WHITESPACE_STRINGS:
            days = MeetingDays(whitespace)

            # check that the dict has all values false
            self.assertDictEqual(days.meeting_days, NO_MEETING_DAYS_DICT)

            # check that the is_async_section flag is true
            self.assertTrue(days.is_async_section)

if __name__ == "__main__":
    unittest.main()