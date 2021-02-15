"""
https://leetcode.com/explore/interview/card/top-interview-questions-hard/116/array-and-strings/827/
"""

from unittest import TestCase

from kevin.leet.product_except_self import Solution, SolutionOptimized


class TestProductExceptSelf(TestCase):
    def _base_test_product_except_self(self, nums, expected):
        for sol_class in [Solution, SolutionOptimized]:
            sol = sol_class()
            actual = sol.product_except_self(nums)
            assert expected == actual, (expected, actual)

    def test_product_except_self_basic(self):
        nums = [1, 2, 3, 4]
        expected = [24, 12, 8, 6]
        self._base_test_product_except_self(nums, expected)
