"""
https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/588/week-1-march-1st-march-7th/3661/
"""

from typing import List

from kevin.utils.bst import TreeNode


class Solution:
    def average_of_levels(self, root: TreeNode) -> List[float]:
        # need to go level by level, so let's do a BFS?
        # add non-None children to the queue
        # pop from start for BFS ordering
        # also have the state encode the level of the given node
        # add that to the running average for each level
        # O(n) BFS runtime to get to each node
        # each average computation should be O(1) if we do things right
        # (could also just do it O(n), that's fine too at first)
        # additional memory complexity would be O(log n) if we just store
        #     current level amounts
        queue = []
        inital_state = (root, 0)  # node, level
        all_vals = [[root.val]]  # list of list of nodes
        queue.append(inital_state)

        while queue:
            current_node, level = queue.pop(0) # pop at 0 for BFS ordering
            current_val = current_node.val

            if len(all_vals) == level:
                # new level
                all_vals.append([current_val])
            else:
                # add to the existing level
                all_vals[level].append(current_val)

            # add non-None children at new levels
            if current_node.left:
                queue.append((current_node.left, level + 1))

            if current_node.right:
                queue.append((current_node.right, level + 1))

        return [sum(vals) / len(vals) for vals in all_vals]


# inspired by:
# https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/588/week-1-march-1st-march-7th/3661/discuss/1094399/Python-simple-bfs-explained
class SolutionOptimized:
    def average_of_levels(self, root: TreeNode) -> List[float]:
        queue = [root]
        result = []

        while queue:
            level = []

            for i in range(len(queue)):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(sum(level) / len(level))

        return result
