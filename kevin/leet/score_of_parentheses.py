"""
https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/587/week-4-february-22nd-february-28th/3651/
"""

class Solution:
    def score_of_parentheses(self, S: str) -> int:
        # recursive approach potentially?
        # need to get down to base cases of (), (A), (AB)
        # know S is balanced
        # len(S) is even - same number of ( and ) in proper stack ordering
        # stack never errors out, stack empty at end of string
        # can we use this?
        if S == '()':
            return 1

        # attempt to find index that splits into A and B case
        # index must be at least 2, and can increment by 2
        for split in range(2, len(S) - 1, 2):
            if self._is_balanced(S[:split]) and self._is_balanced(S[split:]):
                return self.score_of_parentheses(S[:split]) + \
                    self.score_of_parentheses(S[split:])

        # otherwise, must be (A) case
        return 2 * self.score_of_parentheses(S[1:len(S) - 1])

    def _is_balanced(self, s: str) -> bool:
        # return True iff s is balanced
        count = 0
        for c in s:
            if c == '(':
                count += 1
            elif c == ')':
                count -= 1
                if count < 0:
                    return False

        return count == 0


# taken from discussion
# O(n) runtime, O(1) memory - very nice
class SolutionOptimized:
    def score_of_parentheses(self, S: str) -> int:
        ans, bal = 0, 0
        for i, s in enumerate(S):
            bal = bal + 1 if s == "(" else bal - 1
            if i > 0 and S[i-1:i+1] == "()":
                ans += 1 << bal
        return ans
