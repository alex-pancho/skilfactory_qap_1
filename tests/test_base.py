import pytest
from calc import calc_me


def test_add():
    assert 5 == calc_me(3,2,"+")