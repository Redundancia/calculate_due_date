from calculate_due_date import calculate_due_date
from datetime import datetime
import pytest

def test_invalid_submit_date():
    with pytest.raises(ValueError, match="Submit date is not a valid input, try a datetime.datetime type."):
        calculate_due_date("String_input", 12)

def test_invalid_submit_date_negative_int():
    with pytest.raises(ValueError, match="Turnaround time is not a valid input, try a positive integer in hours."):
        calculate_due_date(datetime.now(), -10)

def test_invalid_submit_date_zero():
    with pytest.raises(ValueError, match="Turnaround time is not a valid input, try a positive integer in hours."):
        calculate_due_date(datetime.now(), 0)

def test_invalid_submit_date_not_int():
    with pytest.raises(ValueError, match="Turnaround time is not a valid input, try a positive integer in hours."):
        calculate_due_date(datetime.now(), "11")

def test_invalid_submit_date_not_int():
    with pytest.raises(ValueError, match="Turnaround time is not a valid input, try a positive integer in hours."):
        calculate_due_date(datetime.now(), 1.11)

def test_valid_submit_date_and_turnaround_time_valid_return_type():
    assert isinstance(calculate_due_date(datetime.now(), 12), datetime)

# From friday 10:30 to same day 10:30
def test_valid_0_day():
    assert calculate_due_date(datetime(2022,4,15,10,30), 2) == datetime(2022,4,15,10,30)

# From friday 10:30 to monday 10:30
def test_valid_friday_to_monday():
    assert calculate_due_date(datetime(2022,4,15,10,30), 8) == datetime(2022,4,18,10,30)

# From last friday of month to next months
def test_go_to_next_month():
    assert calculate_due_date(datetime(2022,4,29,10,30), 8) == datetime(2022,5,2,10,30)

# From tuesday to friday
def test_valid_3_day_same_week():
    assert calculate_due_date(datetime(2022,4,12,10,30), 24) == datetime(2022,4,15,10,30)