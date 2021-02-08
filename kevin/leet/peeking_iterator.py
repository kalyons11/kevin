"""
https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/585/week-2-february-8th-february-14th/3633/
"""

from typing import List


class Iterator:
    def __init__(self, nums: List[int]):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """
        self._nums = nums
        self._idx = 0

    
    def has_next(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """
        return self._idx < len(self._nums)

    
    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """
        i = self._idx
        self._idx += 1
        return self._nums[i]


class PeekingIterator:
    def __init__(self, iterator: Iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self._iter = iterator
        self._next = self._iter.next()
        

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self._next
        

    def next(self):
        """
        :rtype: int
        """
        res = self._next
        
        if self._iter.has_next():
            self._next = self._iter.next()
        else:
            self._next = None
        
        return res
        

    def has_next(self):
        """
        :rtype: bool
        """
        return self._next is not None
