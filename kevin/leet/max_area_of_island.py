"""
https://leetcode.com/explore/featured/card/june-leetcoding-challenge-2021/603/week-1-june-1st-june-7th/3764/
"""

from typing import List

"""
taken from:
https://leetcode.com/discuss/explore/june-leetcoding-challenge-2021/1244554/Max-Area-of-Island-or-JS-Python-Java-C%2B%2B-or-Simple-DFS-Recursion-Solution-w-Explanation
"""
class Solution:
    def max_area_of_island(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        best = 0

        def _traverse(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
                return 0

            # "visit" this location
            grid[i][j] = 0
            return 1 + _traverse(i - 1, j) + _traverse(i + 1, j) + \
                _traverse(i, j - 1) + _traverse(i, j + 1)

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    best = max(best, _traverse(i, j))

        return best
