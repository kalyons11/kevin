"""
LeetCode two sum test script.
"""

from unittest import TestCase

from kevin.leet import two_sum


class TestTwoSum(TestCase):
    def test_two_sum(self):
        nums = [3, 2, 4]
        target = 6
        sol = two_sum.Solution()
        assert sorted(sol.two_sum(nums, target)) == [1, 2]
