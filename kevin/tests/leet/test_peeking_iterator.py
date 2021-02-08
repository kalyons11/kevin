"""
https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/585/week-2-february-8th-february-14th/3633/
"""

from typing import List
from unittest import TestCase

from kevin.leet.peeking_iterator import Iterator, PeekingIterator


class TestPeekingIterator(TestCase):
    def _test_peeking_iterator_base(self, nums: List[int]):
        """
        Base test case helper to validate the behavior against a numerical array.
        """

        iter = PeekingIterator(Iterator(nums))
        while iter.has_next():
            val = iter.peek()
            val_next = iter.next()
            assert val == val_next, f'Incorrect behavior for {nums}'

    
    def test_peeking_iterator_basic(self):
        self._test_peeking_iterator_base([1, 2, 3])
