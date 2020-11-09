#!/bin/python

class SparseArray:
    """Class defined by:
    - a collection of input strings named 'strings'
    - a collection of query strings name 'query' """

    def __init__(self, queries, strings):
        self.queries = queries
        self.strings = strings


    def matchingStrings(self):
        q = len(self.queries)
        n = len(self.strings)
        results = [0] * q

        for i in range(0, q):
            query = self.queries[i]
            nb_query_occurrence = 0

            for j in range(0, n):
                string = self.strings[j]
                if query == string:
                    nb_query_occurrence += 1

            results[i] = nb_query_occurrence

        return results
