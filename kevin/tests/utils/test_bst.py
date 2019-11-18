"""
BST utils test script.
"""

from unittest import TestCase

from kevin.utils.bst import Node, BST

class TestBSTUtils(TestCase):
    def test_bst_make(self):
        n = Node(0)
        x = BST(n)

