#!/usr/bin/python3
import unittest

from p1 import getSum

class test(unittest.TestCase):
  def test_sum1(self):
    """
    Test case 1
    """
    data = [17, 18]
    ans = getSum(data)
    self.assertEqual(ans, 35)
    
  def test_sum2(self):
    """
    Test case 2
    """
    data = [100, 1]
    ans = getSum(data)
    self.assertEqual(ans, 101)
    
  def test_sum3(self):
    """
    Test case 3
    """
    data = [55, 55]
    ans = getSum(data)
    self.assertEqual(ans, 110)
    
if __name__ == '__main__':
  unittest.main()
