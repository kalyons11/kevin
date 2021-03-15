"""
https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/
"""

from typing import List
from unittest import TestCase

from kevin.leet.max_sum_bst import Solution
from kevin.utils.bst import BST


class TestMaxSumBST(TestCase):
    def _base_test_max_sum_bst(self, inp_vals: List[int], expected: int):
        sol = Solution()
        inp_tree = BST.init_from_list(inp_vals)
        inp_root = inp_tree.root
        actual = sol.max_sum_bst(inp_root)
        assert expected == actual, (expected, actual)


    def test_max_sum_bst_basic(self):
        inp_vals = [1, 4, 3, 2, 4, 2, 5, None, None, None, None, None, \
            None, 4, 6]
        expected = 20
        self._base_test_max_sum_bst(inp_vals, expected)


    def test_max_sum_bst_tiny(self):
        inp_vals = [4, 3, None, 1, 2]
        expected = 2
        self._base_test_max_sum_bst(inp_vals, expected)


    def test_max_sum_bst_negative(self):
        inp_vals = [-4, -2, -5]
        expected = 0
        self._base_test_max_sum_bst(inp_vals, expected)


    def test_max_sum_bst_tiny_again(self):
        inp_vals = [2, 1, 3]
        expected = 6
        self._base_test_max_sum_bst(inp_vals, expected)


    def test_max_sum_bst_medium(self):
        inp_vals = [5, 4, 8, 3, None, 6, 3]
        expected = 7
        self._base_test_max_sum_bst(inp_vals, expected)
