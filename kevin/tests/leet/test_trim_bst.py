"""
https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/584/week-1-february-1st-february-7th/3626/
"""

from unittest import TestCase

from kevin.leet.trim_bst import Solution
from kevin.utils.bst import BST

class TestTrimBST(TestCase):
    def _base_test_trim_bst(self, inp_vals, low, high, out_vals):
        bst = BST.init_from_list(inp_vals)
        sol = Solution()
        root_new = sol.trim_bst(bst.root, low, high)
        out_actual = BST(root_new).to_list()
        assert out_actual == out_vals, (out_actual, out_vals)

    def test_trim_bst_simple(self):
        inp_vals = [1, 0, 2]
        out_vals = [1, None, 2]
        low = 1
        high = 2
        self._base_test_trim_bst(inp_vals, low, high, out_vals)

    def test_trim_bst_singleton(self):
        inp_vals = [1]
        out_vals = [1]
        low = 1
        high = 2
        self._base_test_trim_bst(inp_vals, low, high, out_vals)

    def test_trim_bst_keep_all(self):
        inp_vals = [1, None, 2]
        out_vals = [1, None, 2]
        low = 1
        high = 3
        self._base_test_trim_bst(inp_vals, low, high, out_vals)

    def test_trim_bst_solo(self):
        inp_vals = [1, None, 2]
        out_vals = [2]
        low = 2
        high = 4
        self._base_test_trim_bst(inp_vals, low, high, out_vals)

    def test_trim_bst_complex(self):
        inp_vals = [3, 0, 4, None, 2, None, None, 1]
        out_vals = [3, 2, None, 1]
        low = 1
        high = 3
        self._base_test_trim_bst(inp_vals, low, high, out_vals)
