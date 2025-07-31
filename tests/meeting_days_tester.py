# import classes from other folders
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.meeting_days import MeetingDays

def days_tester():
    days_string = ["M", "MW", "MWF", "T", "TR", "W", "R", "F", "S", "MTWR", "MTWRF"]

    # test differing string combinations typically found on PatriotWeb
    test_num = 1
    for element in days_string:
        days = MeetingDays()
        days.set_meeting_times(element)
        print("Test " + str(test_num) + ": " + element)
        print(days.meeting_days)
        test_num = test_num + 1
        print()

    # test a whitespace string that is used to denote an asyncronous section
    whitespace_string = [" ", "\n", "\t", "\u00A0"]
    for element in whitespace_string:
        days = MeetingDays()
        days.set_meeting_times(element)
        print("Test " + str(test_num))
        print(days.meeting_days)
        print("is_async_section: " + str(days.is_async_section))
        test_num = test_num + 1
        print()


days_tester()