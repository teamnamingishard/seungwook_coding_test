import unittest
from solve import find_minimum_time

class TestCase1(unittest.TestCase):
  def test_1(self):
    N = 5
    P = [3, 1, 4, 3, 2]
    result = find_minimum_time(N, P)
    self.assertEqual(result, 32)