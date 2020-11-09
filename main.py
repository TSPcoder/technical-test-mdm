#!/bin/python

from util import SparseArray as sp
from util import RandomArrayGenerator as rand

import os
from flask import Flask, jsonify

from flask_restplus import Resource, Api

app = Flask(__name__)
api = Api(app, title='SparseArrays', description='Matching queries with strings')


@api.route('/query/<string:query>')
class MatchingStrings(Resource):

    def get(self, query=''):
        list_results = main(query)
        results_query_occurences = list_results[0]
        strings_array = list_results[1]
        return jsonify({"query occurrences": results_query_occurences,
                        "'strings' array": strings_array})


def main(query):
    # Constructing 'queries' array based on the query string passed as an argument
    queries = query.split(",")
    nb_queries = len(queries)

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

    # Constructing the dictionary result
    results_dict = {}
    for i in range(0, nb_queries):
        results_dict[queries[i]] = results[i]

    # Saving the result in a list of 2 elements
    # - number of query occurences
    # - 'strings' array
    return (results_dict, strings)


if __name__ == "__main__":
    app.run(debug=True)
