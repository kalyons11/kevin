"""
https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/586/week-3-february-15th-february-21st/3641/
"""

from typing import List
from unittest import TestCase

from kevin.leet.k_weakest_rows import Solution, SolutionOptimized


class TestKWeakestRows(TestCase):
    def _base_test_k_weakest_rows(self, mat: List[List[int]], k: int,
                                  expected: List[int]):
        for sol_class in [Solution, SolutionOptimized]:
            sol = sol_class()
            actual = sol.k_weakest_rows(mat, k)
            assert expected == actual, (expected, actual)

    def test_k_weakest_rows_two_ties(self):
        mat = [[1, 1, 0, 0, 0],
               [1, 1, 1, 1, 0],
               [1, 0, 0, 0, 0],
               [1, 1, 0, 0, 0],
               [1, 1, 1, 1, 1]]
        k = 3
        expected = [2, 0, 3]
        self._base_test_k_weakest_rows(mat, k, expected)

    def test_k_weakest_rows_three_ties(self):
        mat = [[1, 0, 0, 0],
               [1, 1, 1, 1],
               [1, 0, 0, 0],
               [1, 0, 0, 0]]
        k = 2
        expected = [0, 2]
        self._base_test_k_weakest_rows(mat, k, expected)
