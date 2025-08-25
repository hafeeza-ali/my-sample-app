# This file contains the tests for our application.

import pytest
from app import add, subtract

def test_add():
    """Tests the add function."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(-5, -5) == -10


def test_subtract():
    """Tests the subtract function."""
    assert subtract(10, 5) == 5
    assert subtract(-1, 1) == -2