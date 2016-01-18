# -*- coding: utf-8 -*-

import unittest
import sorting

class TestSortingMethods(unittest.TestCase):

    A = sorting.Sorting([5,2,4,6,1,3])  # instance of Sorting class unsorted
    A_sorted = list([1, 2, 3, 4, 5, 6]) # sorted list

    ## test case for insertion sort
    def test_insertion(self):
        lst = self.A.insertion()
        self.assertEqual(lst, self.A_sorted)

    ## test case for Merge sort
    def test_merge(self):
        lst = self.A.merge()
        self.assertEqual(lst, self.A_sorted)

    ## test case for Bubble sort
    def test_bubble(self):
        lst = self.A.bubble()
        self.assertEqual(lst, self.A_sorted)

if __name__ == '__main__':
    unittest.main()
