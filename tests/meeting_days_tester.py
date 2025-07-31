# import classes from other folders
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.meeting_days import MeetingDays

def days_tester():
    days_string = ["M", "MW", "MWF", "T", "TR", "W", "R", "F", "S", "MTWR", "MTWRF"]

    # test 1: M
    mon = MeetingDays()
    mon.set_meeting_times(days_string[0])
    print("Test 1: M")
    print(mon.meeting_days)

    print()

    # test 2: MW
    mw = MeetingDays()
    mw.set_meeting_times(days_string[1])
    print("Test 1: MW")
    print(mw.meeting_days)

    print()

    # test 3: MWF
    mwf = MeetingDays()
    mwf.set_meeting_times(days_string[2])
    print("Test 1: MWF")
    print(mwf.meeting_days)

    print()

    # test 4: T
    tues = MeetingDays()
    tues.set_meeting_times(days_string[3])
    print("Test 1: T")
    print(tues.meeting_days)

    print()

    # test 5: TR
    tr = MeetingDays()
    tr.set_meeting_times(days_string[4])
    print("Test 1: TR")
    print(tr.meeting_days)

    print()

    # test 6: W
    wed = MeetingDays()
    wed.set_meeting_times(days_string[5])
    print("Test 1: W")
    print(wed.meeting_days)

    print()

    # test 7: R
    thurs = MeetingDays()
    thurs.set_meeting_times(days_string[6])
    print("Test 1: R")
    print(thurs.meeting_days)

    print()

    # test 8: F
    fri = MeetingDays()
    fri.set_meeting_times(days_string[7])
    print("Test 1: F")
    print(fri.meeting_days)

    print()

    # test 9: S
    sat = MeetingDays()
    sat.set_meeting_times(days_string[8])
    print("Test 1: S")
    print(sat.meeting_days)

    print()

    # test 10: MTWR
    mtwr = MeetingDays()
    mtwr.set_meeting_times(days_string[9])
    print("Test 1: MTWR")
    print(mtwr.meeting_days)

    print()

    # test 11: MTWRF
    mtwrf = MeetingDays()
    mtwrf.set_meeting_times(days_string[10])
    print("Test 1: MTWRF")
    print(mtwrf.meeting_days)


days_tester()