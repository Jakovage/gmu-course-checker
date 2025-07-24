class MeetingDays:
    def __init__(self, monday, tuesday, wednesday, thursday, friday, saturday, sunday):
        # string-boolean dictionary to represent days when a class meets
        self.meeting_days = {
            "Monday": monday,
            "Tuesday": tuesday,
            "Wednesday": wednesday,
            "Thursday": thursday,
            "Friday": friday,
            "Saturday": saturday,
            "Sunday": sunday
        }