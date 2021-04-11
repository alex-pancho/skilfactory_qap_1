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


def test_pow():
    assert calc_me(4, 2, "^") == 16


def test_first_str():
    assert calc_me("a", 9, "/") == "ERROR: now it is does not supported"


def test_second_str():
    assert calc_me(2, "b", "+") == "ERROR: now it is does not supported"


def test_first_none():
    with pytest.raises(ValueError, match="ERROR: send me Number1"):
        calc_me(None, 9, "/")


def test_second_none():
    with pytest.raises(ValueError, match="ERROR: send me Number2"):
        calc_me(2, None, "+")


def test_division_by_zero_with_msg():
    with pytest.raises(ZeroDivisionError, match="ERROR: division by zero!"):
        calc_me(10,0,"/")

def test_unknown_operation():
    with pytest.raises(ValueError, match="ERROR: Unknown operation"):
        calc_me(10,5,"@")