# import classes from other folders
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from course_scraper import CourseScraper
from tests.testing_data import FALL_2025_VALUE, FALL_2025_COURSES
from course import Course

def test_course_scraper():
    # create course scraper object
    scraper = CourseScraper(FALL_2025_VALUE)

    # create course objects from testing data and place it an array
    course_objects =[]
    for data in FALL_2025_COURSES:
        scraped_course = scraper.get_course(*data)
        course_objects.append(scraped_course)

    # print out data
    for data in course_objects:
        print(data)
        print("----")
        print("MeetingDays object:")
        print(data.meeting_days.meeting_days)
        print("----")
        print("is_async_section boolean:")
        print(data.meeting_days.is_async_section)
        print()
    

test_course_scraper()

