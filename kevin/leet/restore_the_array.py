"""
https://leetcode.com/problems/restore-the-array/
"""

# inspired by:
# https://leetcode.com/problems/restore-the-array/discuss/585554/C%2B%2BPython-Simple-DP-with-python
class Solution:
    def number_of_arrays(self, s: str, k: int) -> int:
        # this is going to be hard
        # we could use dynamic programming I guess?
        # need to take substring split points and then see if they are valid
        # going to be exponential though
        # let dp[i] be number of ways to divide string starting at i to end
        # work backwards
        n = len(s)
        dp = [0] * n + [1]
        max_val = 10 ** 9 + 7
        for i in range(n - 1, -1, -1):
            # get numerical value of s[i:]
            j = i + 1
            num = int(s[i:j])
            while j <= n and 1 <= num and num <= k:
                dp[i] = (dp[i] + dp[j]) % max_val
                j += 1
                num = int(s[i:j])

        return dp[0]
