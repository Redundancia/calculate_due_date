from datetime import datetime, timedelta, time

WORKING_HOURS_START = 9
WORKING_HOURS_END = 17
WORKING_HOURS_PER_DAY = 8
DATETIME_FRIDAY_INTEGER = 4

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

    validate_inputs(submit_date, turnaround_time)

    # setup return date variable
    due_date = submit_date

    # while at least a whole working day left, add 1 day to date, and skip weekends if needed
    while turnaround_time >= WORKING_HOURS_PER_DAY:
        due_date = due_date + timedelta(days=+1)
        due_date = skip_weekend_if_needed(due_date)
        turnaround_time -= WORKING_HOURS_PER_DAY

    # we have less than a full workday left, calculate date

    # time left from workdays workhours
    working_time_left_from_day = timedelta(hours=WORKING_HOURS_END) - timedelta(hours=due_date.hour, minutes=due_date.minute, seconds=due_date.second)

    # if due date hours are within day
    if working_time_left_from_day  > timedelta(hours=turnaround_time):
        due_date += timedelta(hours=turnaround_time)
    # if due_date overflows to next day
    else:
        # calculate total delta time, 1 day from overflow plus working hours left
        delta_time = timedelta(days=1,hours=turnaround_time) - working_time_left_from_day
        due_date = datetime.combine(due_date.date(), time(hour=WORKING_HOURS_START,minute=0))
        due_date += delta_time
        due_date = skip_weekend_if_needed(due_date)
    print(due_date)
    return due_date


def validate_inputs(submit_date, turnaround_time):
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
    if submit_date.time() < time(hour=WORKING_HOURS_START, minute=0) or submit_date.time() > time(hour=WORKING_HOURS_END, minute=0):
        raise ValueError("Invalid submit date time, try working hours:9-17.")


def skip_weekend_if_needed(due_date):
    if due_date.weekday() > DATETIME_FRIDAY_INTEGER:
        due_date = due_date + timedelta(days=+2)
    return due_date


if __name__ == "__main__":
    calculate_due_date(datetime(2022,4,29,16,0),15)