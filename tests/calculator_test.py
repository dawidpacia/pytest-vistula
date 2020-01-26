from src.calculator import Calculator

calc = Calculator()

def test_add():
    assert calc.add(1, 2) == 3

