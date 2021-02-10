"""
https://leetcode.com/problems/nim-game/
"""

class Solution:
    def can_win_nim(self, n: int) -> bool:
        # turns out...
        # You can always win a Nim game if the number of stones n in the
        # pile is not divisible by 4.
        return n % 4 != 0
