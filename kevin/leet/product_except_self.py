"""
https://leetcode.com/explore/interview/card/top-interview-questions-hard/116/array-and-strings/827/
"""

from typing import List

# refrenced solution to arrive at this result
class Solution:
    def product_except_self(self, nums: List[int]) -> List[int]:
        """
        no division
        O(n) desired runtime
        *except nums[i]
        brute force would be O(n^2)
        could do even better with a running prefix multiplier, but then would have
            to divide out nums[i] at each step
        n > 1
        don't necessarily know that input is sorted, so can't use that
        dynamic programming?
        with division would be easy...
        two-finger approach? nope, would be O(n^2)
        ...
        we know all products are 32bits, so that isn't an issue to consider rn...
        binary approach?
        # use L and R arrays - was on the right idea there!!!
        """
        N = len(nums)
        L, R = [0] * N, [0] * N
        L[0] = 1
        for i in range(1, N):
            L[i] = L[i - 1] * nums[i - 1]

        R[N - 1] = 1
        for j in reversed(range(N - 1)):
            R[j] = R[j + 1] * nums[j + 1]

        return [L[i] * R[i] for i in range(N)]


class SolutionOptimized:
    def product_except_self(self, nums: List[int]) -> List[int]:
        N = len(nums)
        ans = [0] * N
        ans[0] = 1
        for i in range(1, N):
            ans[i] = ans[i - 1] * nums[i - 1]

        # multiply by things on the right, and update that value R as we go
        R = 1
        for j in reversed(range(N)):
            ans[j] *= R
            R *= nums[j]

        return ans
