#!/bin/python3

#import sys
#sys.path.append('technical-test-mdm/sparse_arrays')
from sparse_arrays import SparseArray


def main():
    strings = ["def", "de", "fgh"]
    queries = ["de", "lmn", "fgh"]

    results = SparseArray.matchingStrings(strings, queries)

    print("Result of matchingStrings when strings = " + str(strings)
          + " and queries = " + str(queries) + ": " + str(results))

if __name__ == "__main__":
    main()





