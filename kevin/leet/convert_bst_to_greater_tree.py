"""
https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/585/week-2-february-8th-february-14th/3634/
"""

from kevin.utils.bst import TreeNode

class Solution:
    def convert_bst(self, root: TreeNode) -> TreeNode:
        # inspired by https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/discuss/1057458/Python%3A-Easy
        self._convert_bst(root)
        return root
        
    def _convert_bst(self, root: TreeNode, current=0) -> int:
        if root is None:
            return current
        
        root.val += self._convert_bst(root.right, current)
        return self._convert_bst(root.left, root.val)
