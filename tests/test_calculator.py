"""Tests for calculator module"""

import pytest
from python.calculator import Calculator

def test_calculator_creation():
    calc = Calculator()
    assert calc is not None

def test_add():
    calc = Calculator()
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0

def test_divide():
    calc = Calculator()
    assert calc.divide(10, 2) == 5
    assert calc.divide(9, 3) == 3

def test_divide_by_zero():
    calc = Calculator()
    with pytest.raises(ValueError):
        calc.divide(10, 0)

def test_get_stats():
    calc = Calculator()
    calc.add(5, 5)
    calc.add(10, 10)
    stats = calc.get_stats()
    assert stats['count'] == 2
    assert stats['sum'] == 30
    assert stats['avg'] == 15
