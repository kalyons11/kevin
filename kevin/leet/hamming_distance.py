"""
https://leetcode.com/problems/hamming-distance/
"""

class Solution:
    def hamming_distance(self, x: int, y: int) -> int:
        # use XOR to compute difference
        diff = x ^ y

        # count number of 1s - just count the set bits
        count = 0
        while diff:
            count += diff & 1
            diff >>= 1 # shift right 1 bit

        return count
