"""
https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/589/week-2-march-8th-march-14th/3669/
"""

# time O(N), where N = len(s)
# memory O(2 ** k)
class Solution:
    def has_all_codes(self, s: str, k: int) -> bool:
        # O(n) solution - gather all length k substrings and check their set
        # has size 2 ** k?
        subs = set()
        for i in range(len(s) - k + 1):
            subs.add(s[i : i + k])
            if len(subs) == 2 ** k:
                return True  # break early

        return False
