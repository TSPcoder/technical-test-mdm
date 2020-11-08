#!/bin/python3

import unittest

from sparse_arrays import matchingStrings

class TestSparseArrays(unittest.TestCase):

    def test_match_queries_with_strings(self):
        strings=["ab","ab","abc"]
        queries=["ab","abc","bc"]
        results = matchingStrings(strings,queries)
        expected = [2,1,0]
        self.assertEqual(expected, results)


if __name__ == '__main__':
    unittest.main()
