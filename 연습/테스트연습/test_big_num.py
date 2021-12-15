import unittest
from big_num import find_big_num

class TestCase(unittest.TestCase):
  def test_1(self):
    input = [123, 456]
    res = find_big_num(input)
    
    self.assertEqual(res, 654)