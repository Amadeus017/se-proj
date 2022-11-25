#!/usr/bin/python3
import unittest

from p1 import getSum

class test(unittest.TestCase):
    
  def test_sum1(self):
    """
    Test case 1
    """
    data = [20, 30 , 40]
    ans = getSum(data)
    self.assertEqual(ans, 60)
    
  def test_sum2(self):
    """
    Test case 2
    """
    data = [0, 0, 0, 0, 0]
    ans = getSum(data)
    self.assertEqual(ans, 5)
    
if __name__ == '__main__':
  unittest.main()
