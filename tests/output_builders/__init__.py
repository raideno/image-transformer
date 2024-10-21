"""
A testing module
"""

from exercises.exercise_1_multiply import mult_two

def test_mult_two():
    """
    A test function
    """
    assert mult_two(3, 2) == 6
    
def test_mult_two_positive_numbers():
    """
    A test function
    """
    assert mult_two(3, 2) == 6
    assert mult_two(1, 1) == 1
    assert mult_two(123456, 654321) == 80779853376

def test_mult_two_with_zero():
    """
    A test function
    """
    assert mult_two(0, 1) == 0
    assert mult_two(0, 0) == 0

def test_mult_two_negative_numbers():
    """
    A test function
    """
    assert mult_two(-1, 5) == -5
    assert mult_two(7, -3) == -21
    assert mult_two(-4, -6) == 24