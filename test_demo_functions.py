# test_demo_functions.py
from demo_functions import add, multiply


def test_add():
    assert add(2, 3) == 5, "Should be 5"
    assert add(-1, 1) == 0, "Should be 0"
    assert add(-1, -1) == -2, "Should be -2"


def test_multiply():
    assert multiply(2, 3) == 6, "Should be 6"
    assert multiply(-1, 1) == -1, "Should be -1"
    assert multiply(-1, -1) == 1, "Should be 1"

def test_false():
    """Always fails."""
    return False
