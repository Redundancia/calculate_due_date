from calendar import THURSDAY
from datetime import datetime, timedelta

def calculate_due_date(submit_date, turnaround_time):
    """
    Inputs: 
    -submit date/time
    -turnaround time in hours(positive integer).
    Working hours are from 9AM to 5PM.
    Working days: Monday to Friday.
    Holidays ignored.
    A problem can only be reported during working hours.
    Returns: the date/time when the issue is resolved. 
    """
    WORKING_HOURS_START = 9
    WORKING_HOURS_END = 17
    WORKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
    WORKING_HOURS_PER_DAY = 8
    
    # validate submite_date type
    if not isinstance(submit_date, datetime):
        raise ValueError("Submit date is not a valid input, try a datetime.datetime type.")

    # validate turnaround_time type
    if not isinstance(turnaround_time, int) or turnaround_time <= 0:
        raise ValueError("Turnaround time is not a valid input, try a positive integer in hours.")

    return datetime.now()

if __name__ == "__main__":
    calculate_due_date(datetime.now(), 1)