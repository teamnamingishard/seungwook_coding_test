import unittest
from solve import minimize_number

class TestCase1(unittest.TestCase):
  def test_1(self):
    input = "55-50+40"
    result = minimize_number(input)
    self.assertEqual(result, -35)
    
  def test_2(self):
    input = "10+20+30+40"
    result = minimize_number(input)
    self.assertEqual(result, 100)
    
  def test_3(self):
    input = "00009-00009"
    result = minimize_number(input)
    self.assertEqual(result, 0)