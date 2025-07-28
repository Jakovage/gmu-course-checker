from utilities.meeting_days import MeetingDays
from utilities.course_type import CourseType
from course import Course

print("hi")

# constants that will be modified
CAP = 100
WAITLST_CAP = 100
REGISTERED = 50
WAITLST_REGISTERED = 0


# create test course and populate with examples
test_course = Course("example")
test_course.update_seat_info(100, 99, 100, 99)
test_course.class_name = "Introduction to Computer Programming"
test_course.class_type = CourseType(1)
test_course.course_code = "CS 110"
test_course.section  = "001"
test_course.start_time = "1:30 PM"
test_course.end_time = "3:00 PM"
test_course.instructor = "David Samudio"
test_course.meeting_days = MeetingDays(True, False, True, False, False, False, False)

# full recitation
full_recitation = Course("example")
full_recitation.capacity = 20
full_recitation.seats_taken =20
full_recitation.waitlist_capacity = 0
full_recitation.waitlist_seats_taken = 0
full_recitation.class_name ="CS 110 recitation"
full_recitation.class_type =CourseType(3)
full_recitation.course_code ="CS 110"
full_recitation.section = "101"
full_recitation.start_time = "9:00 AM"
full_recitation.end_time = "9:50 AM"
full_recitation.instructor = "GTA"
full_recitation.meeting_days = MeetingDays(False, False, False, False, True, False, False)

# available recitation
available_recitation = Course("example")
available_recitation.capacity = 20
available_recitation.seats_taken = 10
available_recitation.waitlist_capacity = 0
available_recitation.waitlist_seats_taken =0
available_recitation.class_name = "CS 110 recitation"
available_recitation.class_type = CourseType(3)
available_recitation.course_code = "CS 110"
available_recitation.section = "102"
available_recitation.start_time = "9:00 AM"
available_recitation.end_time = "9:50 AM"
available_recitation.instructor = "GTA"
available_recitation.meeting_days = MeetingDays(False, False, False, False, True, False, False)

# add recitations to main course
# test_course.linked_courses.append(full_recitation)

def test():
    print(test_course.is_class_available())

# run things
test()