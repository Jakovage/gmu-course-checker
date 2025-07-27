class MeetingDays:
    # constructor with meeting days specified
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

    # update meeting days dict based on scraped meeting days text on PatriotWeb
    def set_meeting_times(self, input_string):
        match input_string:
            case "M":
                self.meeting_days.update({"Monday", True})
            case "MW":
                self.meeting_days.update({"Monday", True})
                self.meeting_days.update({"Wednesday", True})
            case "MWF":
                self.meeting_days.update({"Monday", True})
                self.meeting_days.update({"Wednesday", True})
                self.meeting_days.update({"Friday", True})
            case "T":
                self.meeting_days.update({"Tuesday", True})
            case "TR":
                self.meeting_days.update({"Tuesday", True})
                self.meeting_days.update({"Thursday", True})
            case "W":
                self.meeting_days.update({"Wednesday", True})
            case "R":
                self.meeting_days.update({"Thursday", True})
            case "F":
                self.meeting_days.update({"Friday", True})
            case "S":
                self.meeting_days.update({"Saturday", True})