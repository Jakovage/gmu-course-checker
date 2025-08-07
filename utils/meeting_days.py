class MeetingDays:
    # constructor with meeting days specified
    def __init__(self, input_string):
        # string-boolean dictionary to represent days when a class meets
        self.days_string = input_string
        self.meeting_days = {
            "Monday": False,
            "Tuesday": False,
            "Wednesday": False,
            "Thursday": False,
            "Friday": False,
            "Saturday": False,
            "Sunday": False
        }
        # boolean value to determine if a course is an asynchronous section
        self.is_async_section = False

        self.set_meeting_times(input_string)


    # update meeting days dict based on the scraped meeting days text on PatriotWeb
    def set_meeting_times(self, input_string: str):
        # check if the input string is a whitespace character
        # in PatriotWeb this would indicate that a course is asynchronous
        if not input_string.strip():
            self.is_async_section = True
            return

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
                
    def __str__(self):
        return self.days_string
