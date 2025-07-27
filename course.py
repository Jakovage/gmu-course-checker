from utilities.meeting_days import MeetingDays

class Course:
    def __init__(self, url):
        # basic course info populated from constructor parameters
        self.url = url
        self.course_code = ""
        self.section = ""
        self.class_name = ""
        self.instructor = ""
        self.start_time = ""
        self.end_time = ""
        self.meeting_days = {}
        self.class_type = None

        # other instance variables
        self.linked_courses = []

        # availablity instance variable
        self.capacity = 0
        self.remaining_seats = 0
        self.seats_taken = 0
        self.waitlist_capacity = 0
        self.waitlist_remaining = 0
        self.waitlist_seats_taken = 0

    def update_seat_info(self, capacity, remaining_seats, waitlist_capacity, waitlist_remaining):
        self.capacity = capacity
        self.remaining_seats = remaining_seats
        self.seats_taken = capacity - remaining_seats
        self.waitlist_capacity = waitlist_capacity
        self.waitlist_remaining = waitlist_remaining
        self.waitlist_seats_taken = waitlist_capacity - waitlist_remaining
    
    def is_class_available(self):
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