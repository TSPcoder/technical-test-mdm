#!/bin/python

def matchingStrings(strings, queries):
    q = len(queries)
    n = len(strings)
    results = [0] * q

    for i in range(0, q):
        query = queries[i]
        nbQueryOccurences = 0

        for j in range(0, n):
            string = strings[j]
            if (query == string):
                nbQueryOccurences += 1

        results[i] = nbQueryOccurences

    return results
