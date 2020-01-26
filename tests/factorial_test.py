from src.factorial import factorial


def test_positive():
    assert factorial(4) == 24

def test_zero():
    assert factorial(0) == 1

def test_negative():
    assert factorial(-10) == False
