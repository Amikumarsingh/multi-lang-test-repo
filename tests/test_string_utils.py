"""Tests for string utilities module"""

import pytest
from python.string_utils import (
    reverse_string, capitalize_words, count_vowels,
    is_palindrome, truncate, merge_strings
)

def test_reverse_string():
    assert reverse_string('hello') == 'olleh'
    assert reverse_string('Python') == 'nohtyP'

def test_capitalize_words():
    assert capitalize_words('hello world') == 'Hello World'
    assert capitalize_words('python programming') == 'Python Programming'

def test_count_vowels():
    assert count_vowels('hello') == 2
    assert count_vowels('aeiou') == 5
    assert count_vowels('xyz') == 0

def test_is_palindrome():
    assert is_palindrome('racecar') == True
    assert is_palindrome('hello') == False
    assert is_palindrome('A man a plan a canal Panama') == True

def test_truncate():
    assert truncate('hello world', 5) == 'hello...'
    assert truncate('hi', 10) == 'hi'

def test_merge_strings():
    assert merge_strings('a', 'b', 'c') == 'abc'
    assert merge_strings('hello', ' ', 'world') == 'hello world'
