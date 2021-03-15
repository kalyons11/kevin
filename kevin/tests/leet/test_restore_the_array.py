"""
https://leetcode.com/problems/restore-the-array/
"""

from unittest import TestCase

from kevin.leet.restore_the_array import Solution


class TestRestoreTheArray(TestCase):
    def _base_test_restore_the_array(self, s: str, k: int, expected: int):
        sol = Solution()
        actual = sol.number_of_arrays(s, k)
        assert expected == actual, (expected, actual)


    def test_restore_the_array_basic(self):
        s = '1000'
        k = 10000
        expected = 1
        self._base_test_restore_the_array(s, k, expected)


    def test_restore_the_array_none(self):
        s = '1000'
        k = 10
        expected = 0
        self._base_test_restore_the_array(s, k, expected)


    def test_restore_the_array_medium(self):
        s = '1317'
        k = 2000
        expected = 8
        self._base_test_restore_the_array(s, k, expected)


    def test_restore_the_array_singleton(self):
        s = '2020'
        k = 30
        expected = 1
        self._base_test_restore_the_array(s, k, expected)


    def test_restore_the_array_large(self):
        s = '1234567890'
        k = 90
        expected = 34
        self._base_test_restore_the_array(s, k, expected)
