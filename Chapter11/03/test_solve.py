from unittest import TestCase
from solve import find_minimum_count

class TestCase1(TestCase):
  def test(self):
    s = "0001100"
    result = find_minimum_count(s)
    self.assertEqual(result, 1)
    