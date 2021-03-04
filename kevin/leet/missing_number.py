"""
https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/588/week-1-march-1st-march-7th/3659/
"""

from typing import List


class Solution:
    def missing_number(self, nums: List[int]) -> int:
        # compute the sum
        # subtract from what the sum should really be n(n + 1) / 2
        # where n = len(nums)

        n = len(nums)
        sum_desired = n * (n + 1) // 2 # preserve integer status
        return sum_desired - sum(nums)
