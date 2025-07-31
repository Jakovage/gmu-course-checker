class MeetingDays:
    # constructor with meeting days specified
    def __init__(self):
        # string-boolean dictionary to represent days when a class meets
        self.meeting_days = {
            "Monday": False,
            "Tuesday": False,
            "Wednesday": False,
            "Thursday": False,
            "Friday": False,
            "Saturday": False,
            "Sunday": False
        }

    # update meeting days dict based on the scraped meeting days text on PatriotWeb
    def set_meeting_times(self, input_string):
        # iterate through each char in input_string (e.g "MWF")
        for day in input_string:
            # match day to the corresponding day of the week and update meeting_days
            match day:
                case "M":
                    self.meeting_days["Monday"] = True
                case "T":
                    self.meeting_days["Tuesday"] = True
                case "W":
                    self.meeting_days["Wednesday"] = True
                case "R":
                    self.meeting_days["Thursday"] = True
                case "F":
                    self.meeting_days["Friday"] = True
                case "S":
                    self.meeting_days["Saturday"] = True
