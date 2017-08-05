"""
LeetCode test script.
"""

from unittest import TestCase

from kevin.leet import *


class TestUtils(TestCase):
    def test_two_sum(self):
        nums = [3, 2, 4]
        target = 6
        sol = two_sum.Solution()
        assert sorted(sol.twoSum(nums, target)) == [1, 2]
