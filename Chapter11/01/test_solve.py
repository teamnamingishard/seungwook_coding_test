from unittest import TestCase
from solve import find_maximum_group

class TestCase1(TestCase):
  def test(self):
    n = 5
    x = [2, 3, 1, 2, 2]
    result = find_maximum_group(n, x)
    self.assertEqual(result, 2)
    