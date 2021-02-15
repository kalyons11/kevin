"""
https://leetcode.com/explore/interview/card/top-interview-questions-hard/116/array-and-strings/828/
"""

from typing import List


class Direction:
    RIGHT = 0
    DOWN = 1
    LEFT = 2
    UP = 3


# TODO eventually clean this up - DRY up this code for sure
class Solution:
    def spiral_order(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        dir = Direction.RIGHT

        min_row = 0
        max_row = m - 1
        min_col = 0
        max_col = n - 1

        i, j = 0, 0
        result = []

        while True:
            val = matrix[i][j]
            result.append(val)

            if dir == Direction.RIGHT:
                # try to go right
                if j == max_col:
                    # start going down
                    i += 1
                    min_row += 1
                    dir = Direction.DOWN
                else:
                    # keep going right
                    j += 1

            elif dir == Direction.DOWN:
                # try to go down
                if i == max_row:
                    # start going left
                    j -= 1
                    max_col -= 1
                    dir = Direction.LEFT
                else:
                    # keep going down
                    i += 1

            elif dir == Direction.LEFT:
                # try to go left
                if j == min_col:
                    # start going up
                    i -= 1
                    max_row -= 1
                    dir = Direction.UP
                else:
                    # keep going left
                    j -= 1

            elif dir == Direction.UP:
                # try to go up
                if i == min_row:
                    # start going right
                    j += 1
                    min_col += 1
                    dir = Direction.RIGHT
                else:
                    # keep going up
                    i -= 1

            # check for end case
            if min_row > max_row or min_col > max_col:
                break

        return result
