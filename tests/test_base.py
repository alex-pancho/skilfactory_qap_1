import pytest
from calc import calc_me


def test_add():
    assert calc_me(3,2,"+") == 5

def test_devide_by_zero_wrong():
    assert calc_me(10,0,"/") == "ERROR: Divide by zero!"


def test_devide_by_zero():
    with pytest.raises(ZeroDivisionError):
        calc_me(10,0,"/")

def test_devide_by_zero_with_msg():
    with pytest.raises(ZeroDivisionError, match="ERROR: Divide by zero!"):
        calc_me(10,0,"/")