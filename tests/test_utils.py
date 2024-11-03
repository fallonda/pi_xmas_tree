import pytest
from src.utils import get_days_to_xmas
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
