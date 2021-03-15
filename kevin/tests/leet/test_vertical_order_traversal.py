"""
https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
"""

from typing import List
from unittest import TestCase

from kevin.leet.vertical_order_traversal import Solution
from kevin.utils.bst import BST


class TestVerticalOrderTraversal(TestCase):
    def _base_test_vertical_order_traversal(self, inp_vals: List[int],
                                            expected: List[List[int]]):
        sol = Solution()
        inp_tree = BST.init_from_list(inp_vals)
        inp_root = inp_tree.root
        actual = sol.vertical_traversal(inp_root)
        assert expected == actual, (expected, actual)


    def test_vertical_order_traversal_basic(self):
        inp_vals = [3, 9, 20, None, None, 15, 7]
        expected = [[9], [3, 15], [20], [7]]
        self._base_test_vertical_order_traversal(inp_vals, expected)


    def test_vertical_order_traversal_balanced(self):
        inp_vals = [1, 2, 3, 4, 5, 6, 7]
        expected = [[4], [2], [1, 5, 6], [3], [7]]
        self._base_test_vertical_order_traversal(inp_vals, expected)


    def test_vertical_order_traversal_balanced_swapped(self):
        inp_vals = [1, 2, 3, 4, 6, 5, 7]
        expected = [[4], [2], [1, 5, 6], [3], [7]]
        self._base_test_vertical_order_traversal(inp_vals, expected)
