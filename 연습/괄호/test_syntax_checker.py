import unittest
from syntax_checker import syntax_checker

class Problem1TestCase(unittest.TestCase):
  def test_1(self):
    input = "{(dsadasdf)}"
    res = syntax_checker(input)
    
    self.assertEqual(res, True)
    
  def test_2(self):
    input = "{[a=(b+c)]}"
    res = syntax_checker(input)
    
    self.assertEqual(res, True)
    
  def test_3(self):
    input = ")({}[]"
    res = syntax_checker(input)

    self.assertEqual(res, False)

if __name__ == '__main__':
  unittest.main()