"""
https://leetcode.com/explore/featured/card/february-leetcoding-challenge-2021/586/week-3-february-15th-february-21st/3644/
"""

from typing import List

# improved solutions use recurison/dynamic programming - TODO later

class Solution:
    def number_of_arithmetic_slices(self, A: List[int]) -> int:
        # first, compute all differences
        # then, max contiguous subsequences on the differences array
        diffs = [0] * (len(A) - 1)
        # diffs[i] = A[i + 1] - A[i]
        for i in range(len(A) - 1):
            diffs[i] = A[i + 1] - A[i]

        # assert len(diffs) == len(A) - 1

        # take pairs P, Q where P + 1 < Q
        # check common difference from P through Q inclusive on both ends
        # equivalent to checking only one element in diffs[P] through diffs [Q - 1]
        # if so, we're good
        num_slices = 0
        for p in range(len(A) - 2):
            for q in range(p + 3, len(A) + 1):
                if len(set(diffs[p:q - 1])) == 1:
                    # arithmetic slice!
                    num_slices += 1
                else:
                    # we can break here since we're going to have to adjust p
                    break

        return num_slices
