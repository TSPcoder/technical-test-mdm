#!/bin/python

from util import SparseArray as sp
from util import RandomArrayGenerator as rand

import sys
import os


def main():
    # opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
    args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]

    # Determining the 'queries' array from the input arguments
    queries = []
    nb_queries = 0
    for query in args:
        queries.append(query)
        nb_queries += 1

    # Arguments for generating the random 'strings' array
    min_range = 2
    max_range = 6
    max_length = 2

    # Determining the 'strings' array from the input arguments above
    random_array_generator = rand.RandomArrayGenerator(min_range, max_range, max_length)
    os.environ['STRINGS_ARRAY'] = random_array_generator.getRandomStringArrayGenerator()
    strings = os.getenv('STRINGS_ARRAY').split(",")

    sparse_array = sp.SparseArray(queries, strings)
    results = sparse_array.matchingStrings()

    # Constructing the dictionnary result
    resultsDict = {}
    for i in range(0, nb_queries):
        resultsDict[queries[i]] = results[i]

    print("Number of occurences for which queries array " + str(queries) + " appear in the 'strings' array "
          + str(strings) + " : " + "\n" + str(resultsDict))


if __name__ == "__main__":
    main()
