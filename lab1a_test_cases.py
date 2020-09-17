# CPE 202 Lab 1 Test Cases

import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_01(self):
        tlist = [1,2,3]
        self.assertEqual(max_list_iter(tlist),3)

    def test_max_list_02(self):
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

    def test_reverse(self):
        intlist = [1,2,3]
        revlist = reverse_list(intlist)
        self.assertEqual(revlist,[3,2,1])
        self.assertEqual(intlist,[1,2,3])

    def test_reverse_mutate(self):
        intlist = [1,2,3]
        reverse_list_mutate(intlist)
        self.assertEqual(intlist,[3,2,1])

if __name__ == "__main__":
        unittest.main()