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

    def test_match_queries_with_strings_diff_size(self):
        strings=["abcde","sdaklfj","asdjf","na","basdn","sdaklfj","asdjf","na","asdjf","na","basdn","sdaklfj","asdjf"]
        queries=["abcde","sdaklfj","asdjf","na","basdn"]
        results = matchingStrings(strings,queries)
        expected = [1,3,4,3,2]
        self.assertEqual(expected, results)


if __name__ == '__main__':
    unittest.main()
