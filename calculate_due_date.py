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
    AM_12 = datetime(1,1,1,00,00).time()
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

    # add the rest of the hours to the date
    dueDate += timedelta(hours=turnaround_time)
    
    # if time after workhours, add 1 extra day and extract time difference from hour
    if dueDate.time() > WORKING_HOURS_END:
        dueDate += timedelta(days=1, hours=(WORKING_HOURS_START.hour - WORKING_HOURS_END.hour))

    # If we go into next day, but we are before starting work hours, add a day and extract daily working hours
    if dueDate.time() == AM_12:
        dueDate += timedelta(days=1, hours=-WORKING_HOURS_PER_DAY)

    # skip weekend if needed
    if dueDate.weekday() > DATETIME_FRIDAY_INTEGER:
        dueDate = dueDate + timedelta(days=+2)

    return dueDate

if __name__ == "__main__":
    calculate_due_date(datetime(2022,4,13,15,30),11)