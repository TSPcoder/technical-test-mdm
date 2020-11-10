#!/bin/python

from util import SparseArray as sp
from util import RandomArrayGenerator as rand

import os
from flask import Flask, jsonify
from flask_restplus import Resource, Api
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
api = Api(app, title='SparseArrays', description='Matching queries with strings')

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "SparseArrays Flask API"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)


@api.route('/query/<string:query>')
class MatchingStrings(Resource):

    def get(self, query):
        list_results = main(query)
        results_query_occurences = list_results[0]
        strings_array = list_results[1]
        return jsonify({"query occurrences": results_query_occurences,
                        "'strings' array": strings_array})


def main(query):
    # Constructing 'queries' array based on the query string passed as an argument
    queries = query.split(",")
    nb_queries = len(queries)

    if os.getenv('STRINGS_ARRAY') is None:
        # Generating 'strings' array from the below input arguments
        min_range = 2
        max_range = 6
        max_length = 2
        random_array_generator = rand.RandomArrayGenerator(min_range, max_range, max_length)
        strings = random_array_generator.getRandomArrayGenerator()
    else:
        strings = os.environ['STRINGS_ARRAY'].split(",")

    sparse_array = sp.SparseArray(queries, strings)
    results = sparse_array.matchingStrings()

    # Constructing the dictionary result
    results_dict = {}
    for i in range(0, nb_queries):
        results_dict[queries[i]] = results[i]

    # Saving the result in a list of 2 elements
    # - number of query occurrences
    # - 'strings' array
    return results_dict, strings


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
