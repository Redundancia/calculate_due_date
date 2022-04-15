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
    WORKING_HOURS_START = datetime(1,1,1,9,00).time()
    WORKING_HOURS_END = datetime(1,1,1,17,00).time()
    WORKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
    WORKING_HOURS_PER_DAY = 8
    DATETIME_FRIDAY_INTEGER = 4

    # validate submite_date type
    if not isinstance(submit_date, datetime):
        raise ValueError("Submit date is not a valid input, try a datetime.datetime type.")

    # validate turnaround_time type
    if not isinstance(turnaround_time, int) or turnaround_time <= 0:
        raise ValueError("Turnaround time is not a valid input, try a positive integer in hours.")

    # validate submit date value for weekdays
    if submit_date.weekday() > DATETIME_FRIDAY_INTEGER:
        raise ValueError("Invalid submit date, try weekdays:Mon-Fri.")
    #validate submit date value for working hours
    if submit_date.time() < WORKING_HOURS_START or submit_date.time() > WORKING_HOURS_END:
        raise ValueError("Invalid submit date time, try working hours:9-17.")

    # setup return date variable
    dueDate = submit_date

    # while at least a whole working day left, add 1 day to date, and skip weekends if needed
    while turnaround_time >= WORKING_HOURS_PER_DAY:
        dueDate = dueDate + timedelta(days=+1)
        if dueDate.weekday() > DATETIME_FRIDAY_INTEGER:
            dueDate = dueDate + timedelta(days=+2)
        turnaround_time -= WORKING_HOURS_PER_DAY

    return dueDate

if __name__ == "__main__":
    calculate_due_date(datetime.now(), 1)