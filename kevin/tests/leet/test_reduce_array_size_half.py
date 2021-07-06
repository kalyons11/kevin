"""
https://leetcode.com/explore/featured/card/july-leetcoding-challenge-2021/608/week-1-july-1st-july-7th/3804/
"""

from typing import List
from unittest import TestCase

from kevin.leet.reduce_array_size_half import Solution


class TestReduceArraySizeHalf(TestCase):
    def _base_test_reduce_array_size_half(self, arr: List[int], expected: int):
        sol = Solution()
        actual = sol.min_set_size(arr)
        assert expected == actual, (expected, actual)


    def test_array_reduce_array_size_half_basic(self):
        arr = [3, 3, 3, 3, 5, 5, 5, 2, 2, 7]
        expected = 2
        self._base_test_reduce_array_size_half(arr, expected)


    def test_array_reduce_array_size_half_all_same(self):
        arr = [7, 7, 7, 7, 7, 7]
        expected = 1
        self._base_test_reduce_array_size_half(arr, expected)


    def test_array_reduce_array_size_half_tiny(self):
        arr = [1, 9]
        expected = 1
        self._base_test_reduce_array_size_half(arr, expected)


    def test_array_reduce_array_size_half_medium(self):
        arr = [1000, 1000, 3, 7]
        expected = 1
        self._base_test_reduce_array_size_half(arr, expected)
