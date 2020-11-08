#!/bin/python

import random as rd
import string as s


class RandomArrayGenerator:
    """Class that generates an array of random strings.
    The size of the array is between min_range and max_range.
    The length of the strings is between 1 and max_length"""

    def __init__(self, min_range, max_range, max_length):
        self.min_range = min_range
        self.max_range = max_range
        self.max_length = max_length

    @staticmethod
    def getRandomStringFixedLength(length):
        letters = s.ascii_lowercase
        random_string = ''.join(rd.choice(letters) for _ in range(length))
        return random_string

    def getRandomStringGenerator(self):
        return RandomArrayGenerator.getRandomStringFixedLength(rd.randint(1, self.max_length))

    def getRandomStringArrayGenerator(self):
        array_size = rd.randint(self.min_range, self.max_range)
        generated_string_array = ','.join(self.getRandomStringGenerator() for i in range(0, array_size))
        return generated_string_array

    def getRandomArrayGenerator(self):
        return self.getRandomStringArrayGenerator().split(",")
