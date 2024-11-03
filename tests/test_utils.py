import pytest
from src.utils import get_days_to_xmas, buffer_digit
from datetime import date

def test_get_days_to_xmas_before():
    days = get_days_to_xmas(date(2024,12,20))
    assert days == 5

def test_get_days_to_xmas_on_xmas():
    days = get_days_to_xmas(date(2024,12,25))
    assert days == 0

def test_get_days_to_xmas_on_xmas_old_year():
    days = get_days_to_xmas(date(1999,12,25))
    assert days == 0

def test_get_days_to_xmas_after_xmas():
    days = get_days_to_xmas(date(2024,12,26))
    assert days == 364

def test_get_days_to_xmas_input():
    with pytest.raises(TypeError) as e:
        days = get_days_to_xmas("2024-10-26")
        assert str(e.value) == "only datetime.date type is accepted as input for get_days_to_xmas" 

def test_buffer_digit_one():
    assert buffer_digit(1) == "  1"

def test_buffer_digit_two():
    assert buffer_digit(24)  == " 24"

def test_buffer_digit_three():
    assert buffer_digit(365) == "365"

def test_buffer_digit_too_big():
    with pytest.raises(ValueError) as e:
        buffer_digit(1234)
        assert str(e.value) == "digit input should not be greater than len 3"

def test_buffer_digit_bad_input():
    with pytest.raises(ValueError) as e:
        buffer_digit(1.0)
        assert str(e.value) == "Input to buffer_digit must be int"
