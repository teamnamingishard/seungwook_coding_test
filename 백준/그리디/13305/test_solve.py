from unittest import TestCase
from solve import minimum_price

class TestCase1(TestCase):
  def test_1(self):
    n = 4
    length = [2, 3, 1]
    price = [5, 2, 4, 1]
    result = minimum_price(n, length, price)
    self.assertEqual(result, 18)
    
  def test_2(self):
    n = 4
    length = [3, 3, 4]
    price = [1, 1, 1, 1]
    result = minimum_price(n, length, price)
    self.assertEqual(result, 10)
    