import pytest
from calc import calc_me


def test_add():
    assert calc_me(3, 2, "+") == 5


def test_minus():
    assert calc_me(3, 2, "-") == 1


def test_mul():
    assert calc_me(12345679, 8, "*") == 98765432


def test_div():
    assert calc_me(111111111, 9, "/") == 12345679


def test_division_by_zero_with_msg():
    with pytest.raises(ZeroDivisionError, match="ERROR: division by zero!"):
        calc_me(10,0,"/")

def test_uknown_operation():
    with pytest.raises(ValueError, match="ERROR: Uknown operation"):
        calc_me(10,5,"^")