#!/bin/python3

def matchingStrings(strings, queries):
    q = len(queries)
    n = len(strings)
    results = [0] * q
    for i in range (0, q):
        query = queries[i]
        nbQueryOccurences = 0
        for j in range (0, n):
            string = strings[j]
            if query == string:
                nbQueryOccurences+=1
        results[i] = nbQueryOccurences
    return results

if __name__ == "__main__":
    strings = ["def","de","fgh"]
    queries = ["de","lmn","fgh"]
    print(strings)
    results = matchingStrings(strings, queries)
    print("Result of matchingStrings when strings = " + str(strings)
          + " and queries = " + str(queries) + ": " + str(results))
