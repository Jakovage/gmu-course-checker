# Import statements from other folders and libraries
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.meeting_days import MeetingDays
from utils.course_type import CourseType
from course import Course

# This contains dummy information for a Course object
DUMMY_COURSE = ["example URL", "CS 110", "001", "Introduction to Computer Science", "Mr. Plankton", "7:20 pm - 10:00 pm", MeetingDays(), CourseType(1)]
DUMMY_LINKED_LAB = ["example URL", "CS 110", "101", "CS 110 Lab", "Mr. Plankton", "4:30 pm - 7:10 pm", MeetingDays(), CourseType(2)]
DUMMY_LINKED_RECITATION = ["example URL", "CS 110", "102", "CS 110 Recitation", "Mr. Plankton", "10:30 am - 1:10 pm", MeetingDays(), CourseType(3)]

# A list containing info for a Course object
DUMMY_COURSE_DATA = [DUMMY_COURSE, DUMMY_LINKED_LAB, DUMMY_LINKED_RECITATION]

# These are test values to represent capacity numbers for various scenarios for both lecture sections
# and labs/recitation section
MAX_SEATS = 80
MAX_WAITLIST_SEATS = 99
OPEN_SEATS = 30
OPEN_WAITLIST_SEATS = 15
LINKED_MAX_SEATS = 40
LINKED_OPEN_SEATS = 15

# Dictionary containing various capacity scenarios for a lecture section
# [capacity, remaining seats, waitlist capacity, waitlist remaining]
COURSE_CAPACITIES = {
    "No seats, no waitlist": [MAX_SEATS, 0, 0, 0],
    "No seats, waitlist available": [MAX_SEATS, 0, MAX_WAITLIST_SEATS, OPEN_WAITLIST_SEATS],
    "No seats, waitlist full": [MAX_SEATS, 0, MAX_WAITLIST_SEATS, 0],
    "Open seats only for waitlist": [MAX_SEATS, 1, MAX_WAITLIST_SEATS, OPEN_WAITLIST_SEATS],
    "Available seats": [MAX_SEATS, OPEN_SEATS, MAX_WAITLIST_SEATS, MAX_WAITLIST_SEATS]
}

LINKED_COURSE_CAPACITIES = {
    "No seats, no waitlist": [LINKED_MAX_SEATS, 0, 0, 0],
    "No seats, waitlist available": [LINKED_MAX_SEATS, 0, MAX_WAITLIST_SEATS, LINKED_OPEN_SEATS],
    "No seats, waitlist full": [LINKED_MAX_SEATS, 0, MAX_WAITLIST_SEATS, 0],
    "Open seats only for waitlist": [LINKED_MAX_SEATS, 1, MAX_WAITLIST_SEATS, LINKED_OPEN_SEATS],
    "Available seats": [LINKED_MAX_SEATS, LINKED_OPEN_SEATS, MAX_WAITLIST_SEATS, MAX_WAITLIST_SEATS]
}