"""
https://leetcode.com/explore/featured/card/april-leetcoding-challenge-2021/593/week-1-april-1st-april-7th/3693/
"""

from kevin.utils.link import ListNode


class Solution:
    def is_palindrome(self, head: ListNode) -> bool:
        # naive solution is O(n) time, but requires more than O(1) space
        # because we have to store the whole string up until now or some representation of it
        # how can we do CONSTANT space
        # add back pointers
        # go down and back, that's O(n)
        # can we add something to each node to track a state?
        # that is O(n) space though...
        # we know each value is in the range O(9)
        # just construct a O(9) count dictionary? that should work? in both
        #     directions
        # then, just compare
        # wait, count dictionaries don't work for palindromes
        # let's do O(n) space

        # forward pass
        current = head
        prev = None
        forward = ''
        while current:
            val = current.val
            forward += str(val)
            # add prev pointer
            current.prev = prev
            prev = current
            current = current.next

        # reverse pass = current should be prev, prev doesn't matter now
        current = prev
        reverse = ''
        while current:
            val = current.val
            reverse += str(val)
            current = current.prev  # move backward

        # check equality of strings
        return forward == reverse


class SolutionOptimized:
    def is_palindrome(self, head: ListNode) -> bool:
        # okay, now how do we do this with O(1) additional space?
        # can we link things in a clever way
        # two finger approach?
        # create back pointers, then work in on both sides and check!

        # forward pass to add back pointers
        current = head
        prev = None
        while current:
            # add prev pointer
            current.prev = prev
            prev = current
            current = current.next

        # reverse pass = current should be prev, prev doesn't matter now
        left = head
        right = prev

        # check that left is right, then work in
        # if equal in node value (or one off), can stop
        while True:
            if left.val != right.val:
                return False

            # check exit case
            if left.next == right or left == right:
                return True

            # move
            left = left.next
            right = right.prev
