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
from testing_data import LINKED_COURSE_CAPACITIES

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

def test_linked_courses():
    # test 1: lecture has open seats, recitation has open seats
    course1 = Course(*DUMMY_COURSE_DATA[0])
    course1.update_seat_info(*COURSE_CAPACITIES["Available seats"])
    recitation1 = Course(*DUMMY_COURSE_DATA[2])
    recitation1.update_seat_info(*LINKED_COURSE_CAPACITIES["Available seats"])
    course1.linked_courses.append(recitation1)
    print("Test 1: Lecture open, recitation open")
    print("Expected answer: True")
    print("Actual answer: " + str(course1.is_class_available()))

    print()

    # test 2: lecture has open seats, recitation full
    # (this scenario is impossible if a lecture section has a specific
    # recitation/lab section attached to it)
    course2 = Course(*DUMMY_COURSE_DATA[0])
    course2.update_seat_info(*COURSE_CAPACITIES["Available seats"])
    recitation2 = Course(*DUMMY_COURSE_DATA[2])
    recitation2.update_seat_info(*LINKED_COURSE_CAPACITIES["No seats, no waitlist"])
    course2.linked_courses.append(recitation2)
    print("Test 2: Lecture open, recitation closed")
    print("Expected answer: False")
    print("Actual answer: " + str(course2.is_class_available()))

    print()

    # test 3: lecture has closed seats, recitation open
    # (this scenario can happen if the room the recitation is being held in has a higher
    # capacity than the lecture and that capacities are not manually lowered, though this is unlikely)
    course3 = Course(*DUMMY_COURSE_DATA[0])
    course3.update_seat_info(*COURSE_CAPACITIES["No seats, no waitlist"])
    recitation3 = Course(*DUMMY_COURSE_DATA[2])
    recitation3.update_seat_info(*LINKED_COURSE_CAPACITIES["Available seats"])
    course3.linked_courses.append(recitation3)
    print("Test 3: Lecture closed, recitation open")
    print("Expected answer: False")
    print("Actual answer: " + str(course3.is_class_available()))

    print()

    # test 4: lecture has open seats, one recitation section open, one recitation section closed
    course4 = Course(*DUMMY_COURSE_DATA[0])
    course4.update_seat_info(*COURSE_CAPACITIES["Available seats"])
    recitation4_1 = Course(*DUMMY_COURSE_DATA[2])
    recitation4_1.update_seat_info(*LINKED_COURSE_CAPACITIES["Available seats"])
    recitation4_2 = Course(*DUMMY_COURSE_DATA[2])
    recitation4_2.update_seat_info(*LINKED_COURSE_CAPACITIES["No seats, no waitlist"])
    course4.linked_courses.append(recitation4_1)
    course4.linked_courses.append(recitation4_2)
    print("Test 4: Lecture open, one recitation open, one recitation closed")
    print("Expected answer: True")
    print("Actual answer: " + str(course4.is_class_available()))

    print()

    # test 5: lecture has closed seats, two recitation sections closed
    course5 = Course(*DUMMY_COURSE_DATA[0])
    course5.update_seat_info(*COURSE_CAPACITIES["No seats, no waitlist"])
    recitation5_1 = Course(*DUMMY_COURSE_DATA[2])
    recitation5_1.update_seat_info(*LINKED_COURSE_CAPACITIES["No seats, no waitlist"])
    recitation5_2 = Course(*DUMMY_COURSE_DATA[2])
    recitation5_2.update_seat_info(*LINKED_COURSE_CAPACITIES["No seats, no waitlist"])
    course5.linked_courses.append(recitation5_1)
    course5.linked_courses.append(recitation5_2)
    print("Test 5: Lecture closed, both recitations closed")
    print("Expected answer: False")
    print("Actual answer: " + str(course5.is_class_available()))

    print()

    # test 6: lecture has closed seats, both recitation sections open
    # (this scenario can happen if a course has several recitation sections
    # that are not linked to a specific lecture section, but available to all sections, such
    # as CS 367)
    course6 = Course(*DUMMY_COURSE_DATA[0])
    course6.update_seat_info(*COURSE_CAPACITIES["No seats, no waitlist"])
    recitation6_1 = Course(*DUMMY_COURSE_DATA[2])
    recitation6_1.update_seat_info(*LINKED_COURSE_CAPACITIES["Available seats"])
    recitation6_2 = Course(*DUMMY_COURSE_DATA[2])
    recitation6_2.update_seat_info(*LINKED_COURSE_CAPACITIES["Available seats"])
    course6.linked_courses.append(recitation6_1)
    course6.linked_courses.append(recitation6_2)
    print("Test 5: Lecture closed, both recitations open")
    print("Expected answer: False")
    print("Actual answer: " + str(course6.is_class_available()))


# run tests
test_no_linked_courses()
print()
test_linked_courses()