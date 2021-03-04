"""
https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/588/week-1-march-1st-march-7th/3659/
"""

from typing import List
from unittest import TestCase

from kevin.leet.missing_number import Solution


class TestMissingNumber(TestCase):
    def _base_test_missing_number(self, nums: List[int], expected: int):
        sol = Solution()
        actual = sol.missing_number(nums)
        assert expected == actual, (expected, actual)

    def test_missing_number_singleton(self):
        nums = [0]
        expected = 1
        self._base_test_missing_number(nums, expected)

    def test_missing_number_easy(self):
        nums = [0, 1]
        expected = 2
        self._base_test_missing_number(nums, expected)

    def test_missing_number_medium(self):
        nums = [3, 0, 1]
        expected = 2
        self._base_test_missing_number(nums, expected)

    def test_missing_number_hard(self):
        nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
        expected = 8
        self._base_test_missing_number(nums, expected)
