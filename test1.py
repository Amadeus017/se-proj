#!/usr/bin/python3
import unittest

from p1 import getSum

class test(unittest.Testcase):
  def test_list_int(self):
    """
    Test case 1
    """
    data = [17, 18]
    ans = getSum(data)
    self.assertEqual(ans, 35)
    
if __name__ == '__main__':
  unittest.main()
