# import classes from other folders
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.meeting_days import MeetingDays
from utils.course_type import CourseType
from course import Course


# dummy values for a course
DUMMY_COURSE = ["example URL", "CS 110", "001", "Introduction to Computer Science", "Mr. Plankton", "8:30 AM", "9:45 AM", MeetingDays(True, False, True, False, False, False, False), CourseType(1)]
DUMMY_LINKED_LAB = ["example URL", "CS 110", "101", "CS 110 Lab", "Mr. Plankton", "9:00 AM", "9:50 AM", MeetingDays(False, True, False, False, False, False, False), CourseType(2)]
DUMMY_LINKED_RECITATION = ["example URL", "CS 110", "102", "CS 110 Recitation", "Mr. Plankton", "9:00 AM", "9:50 AM", MeetingDays(False, False, False, True, False, False, False), CourseType(3)]
DUMMY_COURSE_DATA = [DUMMY_COURSE, DUMMY_LINKED_LAB, DUMMY_LINKED_RECITATION]

# capacities [capacity, remaining sets, waitlist capacity, remaining waitlist seats]
COURSE_CAPACITIES = {
    "No seats, no waitlist": [80, 0, 0, 0],
    "No seats, waitlist available": [80, 0, 99, 20],
    "No seats, waitlist full": [80, 0, 99, 0],
    "Open seats only for waitlist": [80, 1, 99, 15],
    "Available seats": [80, 40, 99, 99]
}