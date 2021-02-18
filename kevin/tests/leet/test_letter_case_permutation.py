"""
https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/586/week-3-february-15th-february-21st/3642/
"""

from typing import List
from unittest import TestCase

from kevin.leet.letter_case_permutation import Solution


class TestLetterCasePermutation(TestCase):
    def _base_test_letter_case_permutation(self, inp: str,
                                                 expected: List[str]):
        sol = Solution()
        actual = sol.letter_case_permutation(inp)
        actual_set = set(actual)
        expected_set = set(expected)
        assert expected_set == actual_set, (expected_set, actual_set)

    def test_letter_case_permutation_big(self):
        inp = 'a1b2'
        expected = ['a1b2', 'a1B2', 'A1b2', 'A1B2']
        self._base_test_letter_case_permutation(inp, expected)

    def test_letter_case_permutation_medium(self):
        inp = '3z4'
        expected = ['3z4', '3Z4']
        self._base_test_letter_case_permutation(inp, expected)

    def test_letter_case_permutation_big_digits_only(self):
        inp = '12345'
        expected = ['12345']
        self._base_test_letter_case_permutation(inp, expected)

    def test_letter_case_permutation_single(self):
        inp = '0'
        expected = ['0']
        self._base_test_letter_case_permutation(inp, expected)
