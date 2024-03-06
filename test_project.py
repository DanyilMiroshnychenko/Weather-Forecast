from unittest.mock import patch
import pytest

from project import location_input
from project import is_country_code_valid
from project import messurment_unit
from project import amount_of_days
from project import is_numeric_and_in_range
# from project.project import handle_forecast_data

def test_location_input(monkeypatch):
    inputs = iter(['New York', 'US', 'NY'])

    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    result = location_input()

    assert result == ['New York', 'NY', 'US']

def test_is_country_code_valid():
    assert is_country_code_valid('US') == True
    assert is_country_code_valid('UA') == True
    assert is_country_code_valid('CAN') == True
    assert is_country_code_valid('us') == False  # Lowercase letters
    assert is_country_code_valid('123') == False  # Numeric characters
    assert is_country_code_valid('') == False  # Empty string
    assert is_country_code_valid('A') == False  # Less than 2 characters

def test_messurment_unit(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '1')

    result = messurment_unit()

    assert result == 'metric'

def test_amount_of_days(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '3')

    result = amount_of_days()

    assert result == 3

def test_is_numeric_and_in_range():
    assert is_numeric_and_in_range('3') == True
    assert is_numeric_and_in_range('10') == False
    assert is_numeric_and_in_range('cat') == False











