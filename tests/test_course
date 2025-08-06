# import unit testing
import unittest

# import statements to access other classes
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# import classes from project
from course import Course

# import testing-specific data
from testing_data import DUMMY_COURSE_DATA
from testing_data import COURSE_CAPACITIES
from testing_data import LINKED_COURSE_CAPACITIES

class TestCourse(unittest.TestCase):
    
    def setUp(self):
        # course data indecies
        # these are all purely visual, the logic for checking for course availability
        # does not depend on the CourseType attribute or any other attribute
        # except for the capacity variables and the linked_courses list
        self.COURSE_INDEX = 0
        self.LAB_INDEX = 1
        self.RECITATION_INDEX = 2

    def test_no_linked_courses(self):
        print("Testing courses with no linked sections")
        
        # test 1: open seats
        open_seats_course = Course(*DUMMY_COURSE_DATA[self.COURSE_INDEX])
        open_seats_course.update_seat_info(*COURSE_CAPACITIES["Available seats"])
        print("Test 1: Open seats available")
        self.assertTrue(open_seats_course.is_class_available())

        # test 2: no seats, no watilist
        no_seats_no_waitlist = Course(*DUMMY_COURSE_DATA[self.COURSE_INDEX])
        no_seats_no_waitlist.update_seat_info(*COURSE_CAPACITIES["No seats, no waitlist"])
        print("Test 2: No seats, no waitlist")
        self.assertFalse(no_seats_no_waitlist.is_class_available())

        # test 3: no seats, waitlist available
        no_seats_waitlist_available = Course(*DUMMY_COURSE_DATA[self.COURSE_INDEX])
        no_seats_waitlist_available.update_seat_info(*COURSE_CAPACITIES["No seats, waitlist available"])
        print("Test 3: No seats, waitlist available")
        self.assertFalse(no_seats_waitlist_available.is_class_available())

        # test 4: no seats, waitlist full
        no_seats_waitlist_full = Course(*DUMMY_COURSE_DATA[self.COURSE_INDEX])
        no_seats_waitlist_full.update_seat_info(*COURSE_CAPACITIES["No seats, waitlist full"])
        print("Test 4: No seats, waitlist full")
        self.assertFalse(no_seats_waitlist_full.is_class_available())

        # test 5: open seats only for waitlist
        open_seats_for_waitlist_only = Course(*DUMMY_COURSE_DATA[self.COURSE_INDEX])
        open_seats_for_waitlist_only.update_seat_info(*COURSE_CAPACITIES["Open seats only for waitlist"])
        print("Test 5: Open seats for waitlist only")
        self.assertFalse(open_seats_for_waitlist_only.is_class_available())
    
    def test_single_linked_course(self):
        print("Testing courses with one linked section")

        # Test 1: lecture has open seats, recitation has open seats
        course1 = Course(*DUMMY_COURSE_DATA[self.COURSE_INDEX])
        course1.update_seat_info(*COURSE_CAPACITIES["Available seats"])

        recitation1 = Course(*DUMMY_COURSE_DATA[self.RECITATION_INDEX])
        recitation1.update_seat_info(*LINKED_COURSE_CAPACITIES["Available seats"])
        course1.linked_courses.append(recitation1)
        
        print("Test 1: Lecture open, recitation open")
        self.assertTrue(course1.is_class_available())

        # test 2: lecture has open seats, recitation full
        # (this scenario is impossible if a lecture section has one specific
        # recitation/lab section attached to it)
        course2 = Course(*DUMMY_COURSE_DATA[self.COURSE_INDEX])
        course2.update_seat_info(*COURSE_CAPACITIES["Available seats"])

        recitation2 = Course(*DUMMY_COURSE_DATA[self.RECITATION_INDEX])
        recitation2.update_seat_info(*LINKED_COURSE_CAPACITIES["No seats, no waitlist"])
        course2.linked_courses.append(recitation2)

        print("Test 2: Lecture open, recitation closed")
        self.assertFalse(course2.is_class_available())

        # test 3: lecture has closed seats, recitation open
        # (this scenario can happen if the room the recitation is being held in has a higher
        # capacity than the lecture and that capacities are not manually lowered, though this is unlikely)
        course3 = Course(*DUMMY_COURSE_DATA[self.COURSE_INDEX])
        course3.update_seat_info(*COURSE_CAPACITIES["No seats, no waitlist"])

        recitation3 = Course(*DUMMY_COURSE_DATA[self.RECITATION_INDEX])
        recitation3.update_seat_info(*LINKED_COURSE_CAPACITIES["Available seats"])
        course3.linked_courses.append(recitation3)

        print("Test 3: Lecture closed, recitation open")
        self.assertFalse(course3.is_class_available())

    def test_multiple_linked_courses(self):
        print("Testing courses with multiple linked courses")

        # test 1: lecture has open seats, one recitation section open, one recitation section closed
        course1 = Course(*DUMMY_COURSE_DATA[self.COURSE_INDEX])
        course1.update_seat_info(*COURSE_CAPACITIES["Available seats"])

        recitation1_open = Course(*DUMMY_COURSE_DATA[self.RECITATION_INDEX])
        recitation1_open.update_seat_info(*LINKED_COURSE_CAPACITIES["Available seats"])
        course1.linked_courses.append(recitation1_open)

        recitation1_closed = Course(*DUMMY_COURSE_DATA[self.RECITATION_INDEX])
        recitation1_closed.update_seat_info(*LINKED_COURSE_CAPACITIES["No seats, no waitlist"])
        course1.linked_courses.append(recitation1_closed)

        print("Test 1: Lecture open, two recitations (one open, one closed)")
        self.assertTrue(course1.is_class_available())

        # test 2: lecture has closed seats, two recitation sections closed
        course2 = Course(*DUMMY_COURSE_DATA[self.COURSE_INDEX])
        course2.update_seat_info(*COURSE_CAPACITIES["No seats, no waitlist"])

        recitation2_1 = Course(*DUMMY_COURSE_DATA[self.RECITATION_INDEX])
        recitation2_1.update_seat_info(*LINKED_COURSE_CAPACITIES["No seats, no waitlist"])
        course2.linked_courses.append(recitation2_1)

        recitation2_2 = Course(*DUMMY_COURSE_DATA[self.RECITATION_INDEX])
        recitation2_2.update_seat_info(*LINKED_COURSE_CAPACITIES["No seats, no waitlist"])
        course2.linked_courses.append(recitation2_2)

        print("Test 2: Lecture closed, two recitations (both closed)")
        self.assertFalse(course2.is_class_available())

        # test 3: lecture has closed seats, both recitation sections open
        # (this scenario can happen if a course has several recitation sections
        # that are not linked to a specific lecture section, but available to all sections, such
        # as CS 367)
        course3 = Course(*DUMMY_COURSE_DATA[self.COURSE_INDEX])
        course3.update_seat_info(*COURSE_CAPACITIES["No seats, no waitlist"])

        recitation3_1 = Course(*DUMMY_COURSE_DATA[self.RECITATION_INDEX])
        recitation3_1.update_seat_info(*LINKED_COURSE_CAPACITIES["Available seats"])
        course3.linked_courses.append(recitation3_1)

        recitation3_2 = Course(*DUMMY_COURSE_DATA[self.RECITATION_INDEX])
        recitation3_2.update_seat_info(*LINKED_COURSE_CAPACITIES["Available seats"])    
        course3.linked_courses.append(recitation3_2)

        print("Test 3: Lecture closed, two recitations (both open)")
        self.assertFalse(course3.is_class_available())

if __name__ == "__main__":
    unittest.main()