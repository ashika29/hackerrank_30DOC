# Question link: https://www.hackerrank.com/challenges/30-testing/problem
# Code:

def minimum_index(seq):
    if len(seq) == 0:
        raise ValueError("Cannot get the minimum value index from an empty sequence")
    min_idx = 0
    for i in range(1, len(seq)):
        if seq[i] < seq[min_idx]:
            min_idx = i
    return min_idx
class TestDataEmptyArray(object):
    
    @staticmethod
    def get_array():
        return list()

class TestDataUniqueValues(object):

    @staticmethod
    def get_array():
        return [1,4,10,-2,-7,-10,22]

    @staticmethod
    def get_expected_result():
        return 5

class TestDataExactlyTwoDifferentMinimums(object):

    @staticmethod
    def get_array():
        return [1,4,10,-10,-7,-10,22]

    @staticmethod
    def get_expected_result():
        return 3

