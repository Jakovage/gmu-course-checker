from utils.meeting_days import MeetingDays
from utils.course_type import CourseType

class Course:
    def __init__(self, url: str, course_code: str, section: str, class_name: str, instructior: str, time_period: str, meeting_days: MeetingDays, class_type: CourseType):
        # basic course info populated from constructor parameters
        self.url = url
        self.course_code = course_code
        self.section = section
        self.class_name = class_name
        self.instructor = instructior
        self.time_period = time_period
        self.meeting_days = meeting_days
        self.class_type = class_type

        # list of linked courses
        self.linked_courses = []

        # instance variables that hold capacity info
        self.capacity = 0
        self.remaining_seats = 0
        self.seats_taken = 0
        self.waitlist_capacity = 0
        self.waitlist_remaining = 0
        self.waitlist_seats_taken = 0

    def update_seat_info(self, capacity: int, remaining_seats: int, waitlist_capacity: int, waitlist_remaining: int):
        self.capacity = capacity
        self.remaining_seats = remaining_seats
        self.seats_taken = capacity - remaining_seats
        self.waitlist_capacity = waitlist_capacity
        self.waitlist_remaining = waitlist_remaining
        self.waitlist_seats_taken = waitlist_capacity - waitlist_remaining
    
    def is_class_available(self):
        # check for linked courses (e.g. recitations, labs, etc)
        if len(self.linked_courses) == 0:
            return self.check_self_availability()
        
        # iterate though the linked course and check their availability
        else:
            # check if the course itself is available before checking linked courses
            if self.check_self_availability() == False:
                return False
            else:
                return self.check_linked_courses_availability()
            
    # check if the course itself is available
    def check_self_availability(self):
        # check remaining sets
        if self.remaining_seats > 0:

            # check existence of waitlist
            if self.waitlist_capacity == 0:
                return True
            else:
                # check is anyone is on a waitlist
                if self.waitlist_seats_taken == 0:
                    return True
                else:
                    return False

        # no remaining seats    
        else:
            return False        

    # check if the linked courses are available
    def check_linked_courses_availability(self):
        for linked_course in self.linked_courses:

            # this assumes that only one available linked recitation/lab/etc is needed to register
            # i am not aware of any courses at GMU that requires more than one linked course in order to register
            if linked_course.is_class_available() == True:
                return True
                
        # if none of the linked courses are available, then this course is not available
        return False
            
        