"""
https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/588/week-1-march-1st-march-7th/3661/
"""

from typing import List
from unittest import TestCase

from kevin.leet.average_of_levels import Solution, SolutionOptimized
from kevin.utils.bst import BST


class TestAverageOfLevels(TestCase):
    def _base_test_average_of_levels(self, inp_vals: List[int],
                                     expected: List[float]):
        bst = BST.init_from_list(inp_vals)
        for sol_class in [Solution, SolutionOptimized]:
            sol = sol_class()
            actual = sol.average_of_levels(bst.root)
            assert expected == actual, (expected, actual)

    def test_average_of_levels_easy(self):
        inp_vals = [3, 9, 20, None, None, 15, 7]
        expected = [3, 14.5, 11]
        self._base_test_average_of_levels(inp_vals, expected)

    def test_average_of_levels_singleton(self):
        inp_vals = [9]
        expected = [9]
        self._base_test_average_of_levels(inp_vals, expected)
