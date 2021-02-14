"""
https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/585/week-2-february-8th-february-14th/3636/
"""

class Solution:
    def is_anagram(self, s: str, t: str) -> bool:
        # construct a simple count dictionary and validate equality
        def _construct_count_dict(s: str):
            res = dict()
            for char in s:
                res[char] = res.get(char, 0) + 1
            return res

        return _construct_count_dict(s) == _construct_count_dict(t)
