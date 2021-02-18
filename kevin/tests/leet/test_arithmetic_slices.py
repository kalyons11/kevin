"""
https://leetcode.com/explore/featured/card/february-leetcoding-challenge-2021/586/week-3-february-15th-february-21st/3644/
"""

from typing import List
from unittest import TestCase

from kevin.leet.arithmetic_slices import Solution


class TestArithmeticSlices(TestCase):
    def _base_test_number_of_arithmetic_slices(self, inp: List[int],
                                               expected: int):
        sol = Solution()
        actual = sol.number_of_arithmetic_slices(inp)
        assert expected == actual, (expected, actual)

    def test_number_of_arithmetic_slices_empty(self):
        inp = []
        expected = 0
        self._base_test_number_of_arithmetic_slices(inp, expected)

    def test_number_of_arithmetic_slices_odds(self):
        inp = [1, 3, 5, 7, 9]
        expected = 6
        self._base_test_number_of_arithmetic_slices(inp, expected)

    def test_number_of_arithmetic_slices_simple(self):
        inp = [1, 2, 3, 4]
        expected = 3
        self._base_test_number_of_arithmetic_slices(inp, expected)

    def test_number_of_arithmetic_slices_big(self):
        inp = [1, 2, 3, 8, 9, 10]
        expected = 2
        self._base_test_number_of_arithmetic_slices(inp, expected)
