"""
https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/586/week-3-february-15th-february-21st/3641/
"""

import heapq
from typing import List


class Solution:
    def k_weakest_rows(self, mat: List[List[int]], k: int) -> List[int]:
        # compute sum of each row
        # sort by (row sum, row index) pairs (first by row sum, then by row index)
        # return the top k of that sort
        vals_to_sort = [(sum(mat[i]), i) for i in range(len(mat))]
        vals_sorted = sorted(vals_to_sort)
        indices_sorted = [i for (row_sum, i) in vals_sorted]
        return list(indices_sorted)[:k]


# inspired by:
# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/586/week-3-february-15th-february-21st/3641/discuss/1066695/Python-Binary-Search-+-Heap
class SolutionOptimized:
    def k_weakest_rows(self, mat: List[List[int]], k: int) -> List[int]:
        # let's use binary search to find the sum of each row in log(n) time
        # and, we can use a heap to sort things efficiently
        # first, we define an internal function to compute the sum of a row that is 1-prefixed
        def compute_row_sum(row: List[int]):
            start = -1
            end = len(row)
            while end > start + 1:
                mid = (start + end) // 2
                if(row[mid] == 1):
                    start = mid
                else:
                    end = mid

            return start + 1

        # construct a min-heap with these values
        heap = []
        for i in range(len(mat)):
            heapq.heappush(heap, (-compute_row_sum(mat[i]) , -(i+1)))
            if len(heap) > k:
                heapq.heappop(heap)

        result = []
        while k:
            result.append((-heapq.heappop(heap)[1]) - 1)
            k -= 1
        return result[::-1]
