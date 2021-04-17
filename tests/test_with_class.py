import pytest
from calc import calc_me


class TestCalc:
   def setup(self):
       self.calc = calc_me

   def test_multiply_calculate_correctly(self):
       assert self.calc(2, 3, "*") == 6