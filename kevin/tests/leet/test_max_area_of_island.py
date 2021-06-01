"""
https://leetcode.com/explore/featured/card/june-leetcoding-challenge-2021/603/week-1-june-1st-june-7th/3764/
"""

from typing import List
from unittest import TestCase

from kevin.leet.max_area_of_island import Solution


class TestMaxAreaOfIsland:
    def _base_test_max_area_of_island(self, grid: List[List[int]],
            expected: int):
        sol = Solution()
        actual = sol.max_area_of_island(grid)
        assert expected == actual, (expected, actual)


    def test_max_area_of_island_basic(self):
        grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
        expected = 6
        self._base_test_max_area_of_island(grid, expected)


    def test_max_area_of_island_empty(self):
        grid = [[0,0,0,0,0,0,0,0]]
        expected = 0
        self._base_test_max_area_of_island(grid, expected)
