"""
https://leetcode.com/explore/interview/card/top-interview-questions-hard/116/array-and-strings/828/
"""

from typing import List
from unittest import TestCase

from kevin.leet.spiral_matrix import Solution


class TestSpiralMatrix(TestCase):
    def _base_test_spiral_matrix(self, matrix: List[List[int]], \
                                 expected: List[int]):
        sol = Solution()
        actual = sol.spiral_order(matrix)
        assert expected == actual, (expected, actual)

    def test_spiral_matrix_easy_square(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]
        self._base_test_spiral_matrix(matrix, expected)

    def test_spiral_matrix_medium_rectangle(self):
        matrix = [[1, 2, 3, 4], [5, 6, 7, 8],[9, 10, 11, 12]]
        expected = [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
        self._base_test_spiral_matrix(matrix, expected)

