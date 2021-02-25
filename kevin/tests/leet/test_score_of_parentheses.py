"""
https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/587/week-4-february-22nd-february-28th/3651/
"""

from unittest import TestCase
from kevin.leet.score_of_parentheses import Solution, SolutionOptimized


class TestScoreOfParentheses(TestCase):
    def _base_test_score_of_parentheses(self, inp: str, expected: int):
        for sol_class in [Solution, SolutionOptimized]:
            sol = sol_class()
            actual = sol.score_of_parentheses(inp)
            assert expected == actual, (expected, actual)

    def test_score_of_parentheses_simple(self):
        inp = '()'
        expected = 1
        self._base_test_score_of_parentheses(inp, expected)

    def test_score_of_parentheses_simple_nested(self):
        inp = '(())'
        expected = 2
        self._base_test_score_of_parentheses(inp, expected)

    def test_score_of_parentheses_joined(self):
        inp = '()()'
        expected = 2
        self._base_test_score_of_parentheses(inp, expected)

    def test_score_of_parentheses_complex_nested_joined(self):
        inp = '(()(()))'
        expected = 6
        self._base_test_score_of_parentheses(inp, expected)
