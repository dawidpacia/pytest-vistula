from src.calculator import Calculator

calc = Calculator()

def test_add():
    assert calc.add(1, 2) == 3
    assert calc.add(-1, 1) == 0
