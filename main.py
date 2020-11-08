#!/bin/python

from util import SparseArray as sp

import sys
import os

def main():
    #opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
    args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]

    # Determining the 'queries' array from the input arguments
    queries = []
    nb_queries = 0
    for query in args:
        queries.append(query)
        nb_queries+=1

    #strings = os.getenv('STRINGS_ARRAY')
    strings = ['abc','a','bd']
    sparse_array = sp.SparseArray(queries, strings)

    results = sparse_array.matchingStrings()

    resultsDict = {}
    for i in range (0, nb_queries):
        resultsDict[queries[i]] = results[i]

    print("Number of occurences for which queries array " + str(queries) + " appear in the 'strings' array "
          + str(strings) + " : " + "\n" + str(resultsDict))

if __name__ == "__main__":
    main()





