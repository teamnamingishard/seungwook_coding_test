from unittest import TestCase
from solve import find_minimum_num

class TestCase1(TestCase):
  def test(self):
    n = 5
    x = [3, 2, 1, 1, 9]
    result = find_minimum_num(n, x)
    self.assertEqual(result, 8)
    