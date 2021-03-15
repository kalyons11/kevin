"""
https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
"""

from typing import List

from kevin.utils.bst import TreeNode


class Solution:
    def vertical_traversal(self, root: TreeNode) -> List[List[int]]:
        # this is a hard one - you got this!
        # recursively, maybe?
        # could gather all the nodes
        # then, perform a sort?
        positions = self._generate_positions(root)

        # need to sort first by column, then by row, then by value
        def sort_func(inp):
            node, row, col = inp
            return col, row, node.val

        positions_sorted = sorted(positions, key=sort_func)
        res = []
        current = []
        prev_col = None
        for (node, row, col) in positions_sorted:
            if prev_col is None:
                current.append(node.val)
                prev_col = col
            elif col == prev_col:
                current.append(node.val)
            else:
                res.append(current)
                current = []
                current.append(node.val)
                prev_col = col

        # handle end case
        res.append(current)
        return res


    def _generate_positions(self, root: TreeNode, row: int = 0,
                            col: int = 0):
        res = []
        if not root:
            return res

        res.append((root, row, col))
        res.extend(self._generate_positions(root.left, row + 1, col - 1))
        res.extend(self._generate_positions(root.right, row + 1, col + 1))
        return res
