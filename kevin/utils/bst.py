"""
BST utils.
"""


class Node:
    
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:

    def __init__(self, root):
        self.root = root
