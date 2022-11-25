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
    data = [20, 30 , 40]
    ans = getSum(data)
    self.assertEqual(ans, 60)
    
  def test_sum3(self):
    """
    Test case 3
    """
    data = [100, 1]
    ans = getSum(data)
    self.assertEqual(ans, 101)
    
  def test_sum4(self):
    """
    Test case 4
    """
    data = [0, 0, 0, 0, 0]
    ans = getSum(data)
    self.assertEqual(ans, 5)
    
  def test_sum5(self):
    """
    Test case 5
    """
    data = [55, 55]
    ans = getSum(data)
    self.assertEqual(ans, 110)
    
if __name__ == '__main__':
  unittest.main()
