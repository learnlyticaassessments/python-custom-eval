import pytest
from assignments.assignment1 import add

def test_add():
    # Verify that the add function works as expected.
    assert add(2, 3) == 5, "Expected add(2, 3) to return 5"

def test_add_negative():
    # Verify that the function also handles negative numbers.
    assert add(-1, -1) == -2, "Expected add(-1, -1) to return -2"
