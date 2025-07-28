import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# import classes from project
from utils.meeting_days import MeetingDays
from utils.course_type import CourseType
from course import Course

# import testing-specific data
from testing_data import DUMMY_COURSE_DATA
from testing_data import COURSE_CAPACITIES

# this tests courses that have no linked sections
def no_linked_sections():

    # create class with no linked courses and is full
    no_linked_sections1 = Course("example URL", "CS 110", "100", "Introduction to Computer Science", "Mr. Plankton", "8:30 AM", "9:45 AM", MeetingDays(True, False, True, False, False, False, False), CourseType(1))
    no_linked_sections1.update_seat_info(100, 0, 0, 0)
