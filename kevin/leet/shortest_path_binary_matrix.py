"""
https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/585/week-2-february-8th-february-14th/3638/
"""

from collections import deque
from typing import List


class Solution:
    def shortest_path_binary_matrix(self, grid: List[List[int]]) -> int:
        # BFS will give shortest path solution, guaranteed
        # state is a cell in (r, c) notation, as well as path length to get to that cell
        # state = (r, c, l) where l is the path length
        # only add valid neighbors that have not yet been visited...
        N = len(grid)

        # handle invalid initial state
        initial = (0, 0, 1)
        if grid[0][0] == 1:
            return -1

        visited = set()
        queue = deque([initial])

        while queue:
            (r, c, l) = queue.popleft() # have to pop from front for BFS
            if (r, c) == (N - 1, N - 1):
                return l

            for r_ in range(r - 1, r + 2):
                for c_ in range(c - 1, c + 2):
                    if (r_, c_) == (r, c):
                        continue # ignore the center

                    if r_ >= 0 and r_ < N and c_ >= 0 and c_ < N and \
                            grid[r_][c_] == 0 and (r_, c_) not in visited:
                        visited.add((r_, c_))
                        queue.append((r_, c_, l + 1))

        return -1 # no solution found
