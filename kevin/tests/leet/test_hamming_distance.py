"""
https://leetcode.com/problems/hamming-distance/
"""

from unittest import TestCase

from kevin.leet.hamming_distance import Solution

class TestHammingDistance(TestCase):
    def _base_test_hamming_distance(self, x, y, expected):
        sol = Solution()
        actual = sol.hamming_distance(x, y)
        assert expected == actual, (expected, actual)

    def test_hamming_distance_basic(self):
        self._base_test_hamming_distance(1, 4, 2)

    def test_hamming_distance_identical(self):
        self._base_test_hamming_distance(5, 5, 0)

    def test_hamming_distance_big(self):
        self._base_test_hamming_distance(64, 1, 2)
