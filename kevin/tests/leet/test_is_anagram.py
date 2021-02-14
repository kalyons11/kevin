"""
https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/585/week-2-february-8th-february-14th/3636/
"""

from unittest import TestCase

from kevin.leet.is_anagram import Solution


class TestIsAnagram(TestCase):
    def _base_test_is_anagram(self, s: str, t: str, expected: bool):
        sol = Solution()
        actual = sol.is_anagram(s, t)
        assert expected == actual, (expected, actual)

    def test_is_anagram_easy(self):
        self._base_test_is_anagram('anagram', 'nagaram', True)

    def test_is_anagram_easy_false(self):
        self._base_test_is_anagram('rat', 'car', False)

    def test_is_anagram_easy_false_repeats(self):
        self._base_test_is_anagram('aa', 'a', False)
