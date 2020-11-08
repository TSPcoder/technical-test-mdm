#!/bin/python

import unittest

from util import SparseArray as sp


class TestSparseArrays(unittest.TestCase):

    def test_match_queries_with_strings(self):
        strings = ["ab", "ab", "abc"]
        queries = ["ab", "abc", "bc"]
        sparse_array = sp.SparseArray(queries, strings)

        results = sparse_array.matchingStrings()
        expected = [2, 1, 0]

        self.assertEqual(expected, results)

    def test_match_queries_with_strings_diff_size(self):
        strings = ["abcde", "sdaklfj", "asdjf", "na", "basdn", "sdaklfj", "asdjf", "na", "asdjf", "na", "basdn",
                   "sdaklfj", "asdjf"]
        queries = ["abcde", "sdaklfj", "asdjf", "na", "basdn"]
        sparse_array = sp.SparseArray(queries, strings)

        results = sparse_array.matchingStrings()

        expected = [1, 3, 4, 3, 2]
        self.assertEqual(expected, results)


if __name__ == '__main__':
    unittest.main()
