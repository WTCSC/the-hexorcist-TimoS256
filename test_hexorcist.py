from hexorcist import to_decimal
from hexorcist import from_decimal
import pytest
"""
--- test_hexorcist.py ---
This file contains all unit tests for hexorcist.py, organized into 2 block, one for each major function.

"""
def test_base10_working():
    assert to_decimal('42',10) == 42
def test_base16_working():
    assert to_decimal('1a',16) == 26
def test_base36_working():
    assert to_decimal('4a1', 36) == 5545



def test_to_10():
    assert from_decimal('10','10') == '10'
def test_to_0():
    assert from_decimal('0','22') == '0'
def test_to_30():
    assert from_decimal('296','30') == '9Q'

