from calculate_due_date import calculate_due_date
from datetime import datetime, timedelta
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

def valid_submit_date_and_turnaround_time_valid_return_type():
    assert isinstance(calculate_due_date(datetime.now(), 12), datetime)