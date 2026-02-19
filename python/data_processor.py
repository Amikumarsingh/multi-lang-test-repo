"""Data processor with import and type errors"""

import json
import os
# Missing: import re, datetime

def process_data(data):
    """Process data with type error"""
    # Type error: concatenating string and dict
    return "Data: " + data

def validate_email(email):
    """Validate email - missing re import"""
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None  # NameError

def parse_date(date_str):
    """Parse date - missing datetime import"""
    return datetime.strptime(date_str, '%Y-%m-%d')  # NameError

def load_config(filepath):
    """Load config with logic error"""
    with open(filepath, 'r') as f:
        config = json.load(f)
    # Logic error: wrong comparison
    if config['version'] > '2.0':  # Should use proper version comparison
        return config
    return None

class DataValidator:
    def __init__(self, data):
        self.data = data
    
    def validate(self):
    # Indentation error
        if not self.data:
            return False
        return True
