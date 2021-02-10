"""
https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/584/week-1-february-1st-february-7th/3626/
"""

from kevin.utils.bst import TreeNode

class Solution:
    def trim_bst(self, root: TreeNode, low: int, high: int) -> TreeNode:
        # handle base case of None node
        if not root:
            return None

        # first, check the actual root value itself
        if root.val < low:
            # root is too low - replace with the right child, trimmed again
            return self.trim_bst(root.right, low, high)

        if root.val > high:
            # root is too high - replace with the left child, trimmed again
            return self.trim_bst(root.left, low, high)

        # trim the children if the root is valid
        root.left = self.trim_bst(root.left, low, high)
        root.right = self.trim_bst(root.right, low, high)

        return root
