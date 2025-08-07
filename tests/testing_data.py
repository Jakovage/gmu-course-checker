# Import statements from other folders and libraries
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.meeting_days import MeetingDays
from utils.course_type import CourseType
from course import Course

# This contains dummy information for a Course object
DUMMY_COURSE = ["example URL", "CS 110", "001", "Introduction to Computer Science", "Mr. Plankton", "Horizon Hall", "7:20 pm - 10:00 pm", "  ", CourseType.LECTURE]
DUMMY_LINKED_LAB = ["example URL", "CS 110", "101", "CS 110 Lab", "Mr. Plankton", "Horizon Hall", "4:30 pm - 7:10 pm", "", CourseType.LABORATORY]
DUMMY_LINKED_RECITATION = ["example URL", "CS 110", "102", "CS 110 Recitation", "Mr. Plankton", "Horizon Hall", "10:30 am - 1:10 pm", "M", CourseType.RECITATION]

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

# These are values in the HTML code for the PatriotWeb website that corresponds to a semester
FALL_2025_VALUE = "202570"
SUMMER_2025_VALUE = "202540"

# Array of actual Fall 2025 classes and sections
FALL_2025_COURSES = [["CS", "112", "001"], 
                     ["CS", "262", "004"], 
                     ["MATH", "203", "DL1"],
                     ["MATH", "125", "DL2"],
                     ["CALC", "113", "004"]]

# list of strings to test methods in MeetingDays
SINGLE_DAY_STRINGS = ["M", "T", "W", "R", "F", "S"] 
MULTI_DAY_STRINGS = ["MW", "MWF", "TR", "MTWR", "MTWRF"]
WHITESPACE_STRINGS = [" ", "\n", "\t", "\u00A0"]

# dictionaries that are ment to represent the correct values in meeting_days when
# passing on the string
SINGLE_DAY_DICT_CORRECT = [
    # M
    {
        "Monday": True,
        "Tuesday": False,
        "Wednesday": False,
        "Thursday": False,
        "Friday": False,
        "Saturday": False,
        "Sunday": False
        }, 
    # T
    {
        "Monday": False,
        "Tuesday": True,
        "Wednesday": False,
        "Thursday": False,
        "Friday": False,
        "Saturday": False,
        "Sunday": False
    }, 
    # W
    {
        "Monday": False,
        "Tuesday": False,
        "Wednesday": True,
        "Thursday": False,
        "Friday": False,
        "Saturday": False,
        "Sunday": False
    }, 
    # R
    {
        "Monday": False,
        "Tuesday": False,
        "Wednesday": False,
        "Thursday": True,
        "Friday": False,
        "Saturday": False,
        "Sunday": False
    }, 
    # F
    {
        "Monday": False,
        "Tuesday": False,
        "Wednesday": False,
        "Thursday": False,
        "Friday": True,
        "Saturday": False,
        "Sunday": False
    }, 
    # S
    {
        "Monday": False,
        "Tuesday": False,
        "Wednesday": False,
        "Thursday": False,
        "Friday": False,
        "Saturday": True,
        "Sunday": False
    }
]

MULTI_DAY_DICT_CORRECT = [
    # MW
    {
        "Monday": True,
        "Tuesday": False,
        "Wednesday": True,
        "Thursday": False,
        "Friday": False,
        "Saturday": False,
        "Sunday": False
        }, 
    # MWF
    {
        "Monday": True,
        "Tuesday": False,
        "Wednesday": True,
        "Thursday": False,
        "Friday": True,
        "Saturday": False,
        "Sunday": False
    }, 
    # TR
    {
        "Monday": False,
        "Tuesday": True,
        "Wednesday": False,
        "Thursday": True,
        "Friday": False,
        "Saturday": False,
        "Sunday": False
    }, 
    # MTWR
    {
        "Monday": True,
        "Tuesday": True,
        "Wednesday": True,
        "Thursday": True,
        "Friday": False,
        "Saturday": False,
        "Sunday": False
    }, 
    # MTWRF
    {
        "Monday": True,
        "Tuesday": True,
        "Wednesday": True,
        "Thursday": True,
        "Friday": True,
        "Saturday": False,
        "Sunday": False
    }
]

NO_MEETING_DAYS_DICT =  {
    "Monday": False,
    "Tuesday": False,
    "Wednesday": False,
    "Thursday": False,
    "Friday": False,
    "Saturday": False,
    "Sunday": False
}

# these are lists of actual courses that are currently available and unavailable
# as of August 6th, 2025
FALL_2025_AVAIL_COURSES = [["CS", "571", "002"],
                           ["CS", "110", "001"],
                           ["CS", "310", "001"]]

FALL_2025_UNAVAIL_COURSES = [["CS", "330", "003"],
                             ["CS", "471", "002"],
                             ["CS", "262", "003"]]

