"""
BST utils test script.
"""

from unittest import TestCase

from kevin.utils.bst import BST, TreeNode

class TestBSTUtils(TestCase):
    def test_bst_make(self):
        n = TreeNode(0)
        x = BST(n)

    def test_init_from_list_empty_should_fail(self):
        keys = []
        with self.assertRaises(ValueError):
            BST.init_from_list(keys)

    def test_init_from_list_basic(self):
        keys = [1, 2, 3, None, None, 4, None, None, 5]
        bst = BST.init_from_list(keys)
        assert bst.root.val == 1
        assert bst.root.left.val == 2
        assert bst.root.right.val == 3
        assert bst.root.right.left.right.val == 5

    def test_to_list_single(self):
        bst = BST(TreeNode(0))
        out = bst.to_list()
        assert out == [0], out

    def test_to_list_multiple(self):
        bst = BST(TreeNode(1, TreeNode(0), TreeNode(2, None, TreeNode(3))))
        out = bst.to_list()
        assert out == [1, 0, 2, None, None, None, 3], out
