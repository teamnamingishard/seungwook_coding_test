import unittest
from add import add

class Problem2TestCase(unittest.TestCase):
  def test_1(self):
    input = [1, 2, 3, 4, 5]
    res = add(input)
    
    self.assertEqual(res, 15)
    

if __name__ == '__main__':
  unittest.main()