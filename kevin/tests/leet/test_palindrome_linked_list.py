"""
https://leetcode.com/explore/featured/card/april-leetcoding-challenge-2021/593/week-1-april-1st-april-7th/3693/
"""

from typing import List
from unittest import TestCase

from kevin.leet.palindrome_linked_list import Solution, SolutionOptimized
from kevin.utils.link import LinkedList


class TestPalindromeLinkedList(TestCase):
    def _base_test_palindrome_linked_list(self, inp_vals: List[int],
                                          expected: bool):
        for sol_class in [Solution, SolutionOptimized]:
            sol = sol_class()
            inp = LinkedList.init_from_list(inp_vals)
            head = inp.head
            actual = sol.is_palindrome(head)
            assert expected == actual, (expected, actual)


    def test_palindrome_linked_list_singleton(self):
        inp_vals = [1]
        expected = True
        self._base_test_palindrome_linked_list(inp_vals, expected)


    def test_palindrome_linked_list_medium_true(self):
        inp_vals = [1, 2, 2, 1]
        expected = True
        self._base_test_palindrome_linked_list(inp_vals, expected)


    def test_palindrome_linked_list_small_false(self):
        inp_vals = [1, 2]
        expected = False
        self._base_test_palindrome_linked_list(inp_vals, expected)
