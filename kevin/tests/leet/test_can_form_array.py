"""
LeetCode can form array test script.
https://leetcode.com/explore/featured/card/january-leetcoding-challenge-2021/579/week-1-january-1st-january-7th/3589/
"""

from unittest import TestCase

from kevin.leet import can_form_array


class TestCanFormArray(TestCase):
    def assert_can_form_array_result(self, arr, pieces, result):
        sol = can_form_array.Solution()
        result_actual = sol.can_form_array(arr, pieces)
        assert result_actual == result

    def test_can_form_array_easy(self):
        arr = [85]
        pieces = [[85]]
        self.assert_can_form_array_result(arr, pieces, True)

    def test_can_form_array_medium(self):
        arr = [15, 88]
        pieces = [[88], [15]]
        self.assert_can_form_array_result(arr, pieces, True)

    def test_can_form_array_cannot_easy(self):
        arr = [49, 18, 16]
        pieces = [[16, 18, 49]]
        self.assert_can_form_array_result(arr, pieces, False)

    def test_can_form_array_hard(self):
        arr = [91, 4, 64, 78]
        pieces = [[78], [4, 64], [91]]
        self.assert_can_form_array_result(arr, pieces, True)

    def test_can_form_array_not_exists(self):
        arr = [1, 3, 5, 7]
        pieces = [[2, 4, 6, 8]]
        self.assert_can_form_array_result(arr, pieces, False)
