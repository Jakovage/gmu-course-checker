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

# testing without any linked courses
def test_no_linked_courses():
    # test 1: open seats
    open_seats_course = Course(*DUMMY_COURSE_DATA[0])
    open_seats_course.update_seat_info(*COURSE_CAPACITIES["Available seats"])
    print("Test 1: Open seats available")
    print("Expected answer: True")
    print("Actual answer: " + str(open_seats_course.is_class_available()))

    print()

    # test 2: no seats, no watilist
    no_seats_no_waitlist = Course(*DUMMY_COURSE_DATA[0])
    no_seats_no_waitlist.update_seat_info(*COURSE_CAPACITIES["No seats, no waitlist"])
    print("Test 2: No seats, no waitlist")
    print("Expected answer: False")
    print("Actual answer: " + str(no_seats_no_waitlist.is_class_available()))

    print()

    # test 3: no seats, waitlist available
    no_seats_waitlist_available = Course(*DUMMY_COURSE_DATA[0])
    no_seats_waitlist_available.update_seat_info(*COURSE_CAPACITIES["No seats, waitlist available"])
    print("Test 3: No seats, waitlist available")
    print("Expected answer: False")
    print("Actual answer: " + str(no_seats_waitlist_available.is_class_available()))

    print()

    # test 4: no seats, waitlist full
    no_seats_waitlist_full = Course(*DUMMY_COURSE_DATA[0])
    no_seats_waitlist_full.update_seat_info(*COURSE_CAPACITIES["No seats, waitlist full"])
    print("Test 4: No seats, waitlist full")
    print("Expected answer: False")
    print("Actual answer: " + str(no_seats_waitlist_full.is_class_available()))   

    print()

    # test 5: open seats only for waitlist
    open_seats_for_waitlist_only = Course(*DUMMY_COURSE_DATA[0])
    open_seats_for_waitlist_only.update_seat_info(*COURSE_CAPACITIES["Open seats only for waitlist"])
    print("Test 5: Open seats for waitlist only")
    print("Expected answer: False")
    print("Actual answer: " + str(open_seats_for_waitlist_only.is_class_available()))  


# run tests
test_no_linked_courses()