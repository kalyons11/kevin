"""
https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/585/week-2-february-8th-february-14th/3639/
"""

from typing import List


class Solution:
    def is_bipartite(self, graph: List[List[int]]) -> bool:
        # depth first search on graph
        # color each node 0 or 1 depending on the parent
        # if we can complete the search without violating a coloring,
        # return True
        coloring = dict() # maps a node to a "color", which is 0 or 1
        # referring to the side of the graph this node would appear on in a
        # bipartite mapping
        initial_state = (0, 0)
        queue = [initial_state] # list of (node, color) pairs, where node
        # is an index into the graph
        visited = set() # keep track of a visited set of nodes

        # graph is not necessarily connected
        # need to make sure that we populate more nodes if needed
        while queue:
            node, color = queue.pop() # DFS, LIFO

            # visit this node
            visited.add(node)

            if node in coloring and coloring[node] != color:
                return False # found an inconsistency

            # set the color in our map
            coloring[node] = color

            # add all neighbors to the queue with the opposite color
            neighbor_color = 1 if color == 0 else 0
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append((neighbor, neighbor_color))

            # check if we run into the end of a connected component
            if not queue and len(visited) != len(graph):
                # find the first non-visited node and go there
                for node in range(len(graph)):
                    if node not in visited:
                        queue.append((node, 0))
                        break

        return True

