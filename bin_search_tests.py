import unittest
from bin_search import *
from typing import List

class TestLab1b(unittest.TestCase):

    def test_bin_search_iter_01(self):
        tlist: List = [5, 9, 18, 23, 55, 72]
        self.assertEqual(bin_search_iter(tlist, 5), 0)

    def test_bin_search_iter_02(self):
        tlist = None
        with self.assertRaises(ValueError):  # uses context manager for checking exception
            bin_search_iter(tlist, 5)

if __name__ == "__main__":
        unittest.main()
