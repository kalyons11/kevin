"""
https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/589/week-2-march-8th-march-14th/3666/
"""

from collections import deque

from kevin.utils.bst import TreeNode


class Solution:
    def add_one_row(self, root: TreeNode, v: int, d: int) -> TreeNode:
        # do BFS until we hit the proper depth
        # if we are over the depth, stop! (improve runtime)
        # then, just perform the proper updates to the tree at this given
        # level

        # handle base case where we need to add at root
        if d == 1:
            new_root = TreeNode(v)
            new_root.left = root
            return new_root

        queue = deque([(root, 1)]) # node, depth

        while queue:
            node, depth = queue.popleft() # for BFS FIFO ordering
            if depth == d - 1:
                # perform update here
                new_node_left = TreeNode(v)
                new_node_right = TreeNode(v)
                new_node_left.left = node.left
                new_node_right.right = node.right
                node.left = new_node_left
                node.right = new_node_right

            elif depth < d - 1:
                # add child nodes to queue with higher depth
                if node.left: queue.append((node.left, depth + 1))
                if node.right: queue.append((node.right, depth + 1))

            else:
                assert depth > d - 1
                # should be able to break now
                # since we are doing BFS, we have visited all nodes at d - 1
                break

        return root
