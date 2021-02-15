"""
https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/585/week-2-february-8th-february-14th/3638/
"""

import json
import os
from typing import List
from unittest import TestCase

from kevin.leet.shortest_path_binary_matrix import Solution


class TestShortestPathBinaryMatrix(TestCase):
    def _base_test_shortest_path_binary_matrix(self, grid: List[List[int]],
                                               expected):
        sol = Solution()
        actual = sol.shortest_path_binary_matrix(grid)
        assert expected == actual, (expected, actual)

    def test_shortest_path_binary_matrix_easy_square(self):
        grid = [[0, 1], [1, 0]]
        expected = 2
        self._base_test_shortest_path_binary_matrix(grid, expected)

    def test_shortest_path_binary_matrix_medium_square(self):
        grid = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
        expected = 4
        self._base_test_shortest_path_binary_matrix(grid, expected)

    def test_shortest_path_binary_matrix_massive(self):
        fname_file = 'data/big_matrix.txt'
        dirname_file = os.path.dirname(__file__)
        fname_full = os.path.join(dirname_file, os.pardir, fname_file)
        with open(fname_full, 'r') as f:
            grid = json.load(f)
            expected = 146
            self._base_test_shortest_path_binary_matrix(grid, expected)

