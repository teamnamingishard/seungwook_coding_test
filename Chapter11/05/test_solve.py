from unittest import TestCase
from solve import find_combination

class TestCase1(TestCase):
  def test_1(self):
    n, m = 5, 3
    data = [1, 3, 2, 3, 2]
    result = find_combination(n, m, data)
    self.assertEqual(result, 8)
    
  def test_2(self):
    n, m = 8, 5
    data = [1, 5, 4, 3, 2, 4, 5, 2]
    result = find_combination(n, m, data)
    self.assertEqual(result, 25)
    