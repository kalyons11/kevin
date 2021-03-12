"""
https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/589/week-2-march-8th-march-14th/3669/
"""

from unittest import TestCase
from kevin.leet.check_binary_codes import Solution


class TestCheckBinaryCodes(TestCase):
    def _base_test_check_binary_codes(self, s: str, k: int, expected: bool):
        sol = Solution()
        actual = sol.has_all_codes(s, k)
        assert expected == actual, (expected, actual)

    def test_check_binary_codes_basic(self):
        s = '00110110'
        k = 2
        expected = True
        self._base_test_check_binary_codes(s, k, expected)

    def test_check_binary_codes_medium(self):
        s = '00110'
        k = 2
        expected = True
        self._base_test_check_binary_codes(s, k, expected)

    def test_check_binary_codes_tiny_true(self):
        s = '0110'
        k = 1
        expected = True
        self._base_test_check_binary_codes(s, k, expected)

    def test_check_binary_codes_tiny_false(self):
        s = '0110'
        k = 2
        expected = False
        self._base_test_check_binary_codes(s, k, expected)

    def test_check_binary_codes_big_false(self):
        s = '0000000001011100'
        k = 4
        expected = False
        self._base_test_check_binary_codes(s, k, expected)
