from hexorcist import to_decimal
from hexorcist import from_decimal
import pytest

def test_base10_working():
    assert to_decimal('42',10) == 42
def test_base16_working():
    assert to_decimal('1a',16) == 26
def test_base36_working():
    assert to_decimal('4a1', 36) == 5545
def test_bad_input():
    assert to_decimal(['this',15,"a",'list', ('and','not'), 'a str'], 69) == "input type error"
def test_bad_base():
    assert to_decimal('42',{}) == "bass type error"

def test_to_b10():
    assert from_decimal('10','10') == 10
def test_to_0():
    assert from_decimal('0','22') == 10
def test_wrong_input():
    assert from_decimal(['a'],'22') == "input type error"
def test_wrong_base():
    assert from_decimal('a', {7}) == "bass type error"
