"""
https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/589/week-2-march-8th-march-14th/3671/
"""

from typing import List
from unittest import TestCase

from kevin.leet.swap_nodes import Solution, SolutionOptimized
from kevin.utils.link import LinkedList


class TestSwapNodes(TestCase):
    def _base_test_swap_nodes(self, inp_vals: List[int], k: int,
                              expected_vals: List[int]):
        for sol_class in [Solution, SolutionOptimized]:
            sol = sol_class()
            inp_list = LinkedList.init_from_list(inp_vals)
            inp_head = inp_list.head
            actual_head = sol.swap_nodes(inp_head, k)
            actual_vals = LinkedList(actual_head).to_list()
            assert expected_vals == actual_vals, \
                (expected_vals, actual_vals)

    def test_swap_nodes_simple(self):
        inp_vals = [1, 2, 3, 4, 5]
        k = 2
        expected_vals = [1, 4, 3, 2, 5]
        self._base_test_swap_nodes(inp_vals, k, expected_vals)

    def test_swap_nodes_big(self):
        inp_vals = [7, 9, 6, 6, 7, 8, 3, 0, 9, 5]
        k = 5
        expected_vals = [7, 9, 6, 6, 8, 7, 3, 0, 9, 5]
        self._base_test_swap_nodes(inp_vals, k, expected_vals)

    def test_swap_nodes_singleton(self):
        inp_vals = [1]
        k = 1
        expected_vals = [1]
        self._base_test_swap_nodes(inp_vals, k, expected_vals)

    def test_swap_nodes_tiny(self):
        inp_vals = [1, 2]
        k = 1
        expected_vals = [2, 1]
        self._base_test_swap_nodes(inp_vals, k, expected_vals)

    def test_swap_nodes_medium(self):
        inp_vals = [1, 2, 3]
        k = 2
        expected_vals = [1, 2, 3]
        self._base_test_swap_nodes(inp_vals, k, expected_vals)
