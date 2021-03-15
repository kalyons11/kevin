"""
https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/
"""

from kevin.utils.bst import TreeNode


# inspired by:
# https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/discuss/533254/python-easy-to-understand-divide-and-conquer
# this is a tough one!
class Solution:
    def max_sum_bst(self, root: TreeNode) -> int:
        return self.helper(root)[0]


    def helper(self, root: TreeNode):
        # max sum, current sum, min max of sub tree
        # handle null case
        if not root:
            return 0, 0, float('inf'), float('-inf')

        left_sum, left_current, left_min, left_max = self.helper(root.left)
        right_sum, right_current, right_min, right_max = self.helper(root.right)

        # check if not valid BST
        if root.val <= left_max or root.val >= right_min:
            # invalid since we break the BST invariant
            return max(left_sum, right_sum), float('-inf'), float('-inf'), \
                float('inf')

        # update current sums, since we are a BST
        root_current = left_current + right_current + root.val
        return max(left_sum, right_sum, root_current), root_current, \
            min(left_min, root.val), max(root.val, right_max)
