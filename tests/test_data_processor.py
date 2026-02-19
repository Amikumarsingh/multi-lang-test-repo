"""Tests for data processor module"""

import pytest
from python.data_processor import (
    process_data, validate_email, parse_date, 
    load_config, DataValidator
)

def test_process_data():
    data = {'key': 'value'}
    result = process_data(data)
    assert 'Data:' in result

def test_validate_email():
    assert validate_email('test@example.com') == True
    assert validate_email('invalid') == False

def test_parse_date():
    date = parse_date('2024-01-15')
    assert date is not None

def test_data_validator():
    validator = DataValidator({'test': 'data'})
    assert validator.validate() == True
    
def test_data_validator_empty():
    validator = DataValidator(None)
    assert validator.validate() == False
