"""
https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/585/week-2-february-8th-february-14th/3634/
"""

from unittest import TestCase

from kevin.leet.convert_bst_to_greater_tree import Solution
from kevin.utils.bst import BST, TreeNode

class TestConvertBSTToGreaterTree(TestCase):
    def _base_test_convert_bst_to_greater_tree(self, inp_vals, out_vals):
        bst = BST.init_from_list(inp_vals)
        sol = Solution()
        sol.convert_bst(bst.root)
        sol_list = bst.to_list()
        assert sol_list == out_vals, (sol_list, out_vals)

    def test_convert_bst_to_greater_tree_basic(self):
        inp_vals = [0, None, 1]
        out_vals = [1, None, 1]
        self._base_test_convert_bst_to_greater_tree(inp_vals, out_vals)

    def test_convert_bst_to_greater_tree_small(self):
        inp_vals = [1, 0, 2]
        out_vals = [3, 3, 2]
        self._base_test_convert_bst_to_greater_tree(inp_vals, out_vals)

    def test_convert_bst_to_greater_tree_medium(self):
        inp_vals = [3, 2, 4, 1]
        out_vals = [7, 9, 4, 10]
        self._base_test_convert_bst_to_greater_tree(inp_vals, out_vals)

    def test_convert_bst_to_greater_tree_large(self):
        inp_vals = [4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None,
                    None, 8]
        out_vals = [30, 36, 21, 36, 35, 26, 15, None, None, None, 33, None,
                    None, None, 8]
        self._base_test_convert_bst_to_greater_tree(inp_vals, out_vals)
