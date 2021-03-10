"""
https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/589/week-2-march-8th-march-14th/3666/
"""

from typing import List
from unittest import TestCase

from kevin.leet.add_one_row import Solution
from kevin.utils.bst import BST, TreeNode


class TestAddOneRow(TestCase):
    def _base_test_add_one_row(self, inp_vals: List[int], v: int, d: int,
                               expected: List[int]):
        sol = Solution()
        tree = BST.init_from_list(inp_vals)
        root = tree.root
        actual_root = sol.add_one_row(root, v, d)
        actual_vals = BST(actual_root).to_list()
        assert expected == actual_vals, (expected, actual_vals)

    def test_add_one_row_basic(self):
        inp_vals = [4, 2, 6, 3, 1, 5, None]
        v = 1
        d = 2
        expected = [4, 1, 1, 2, None, None, 6, 3, 1, 5]
        self._base_test_add_one_row(inp_vals, v, d, expected)

    def test_add_one_row_medium(self):
        inp_vals = [4, 2, None, 3, 1]
        v = 1
        d = 3
        expected = [4, 2, None, 1, 1, 3, None, None, 1]
        self._base_test_add_one_row(inp_vals, v, d, expected)
