from unittest import TestCase
from solve import plus_or_multiply

class TestCase1(TestCase):
  def test_1(self):
    s = "02984"
    result = plus_or_multiply(s)
    self.assertEqual(result, 576)
    
  def test_2(self):
    s = "567"
    result = plus_or_multiply(s)
    self.assertEqual(result, 210)
    