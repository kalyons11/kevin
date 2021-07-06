"""
https://leetcode.com/explore/featured/card/july-leetcoding-challenge-2021/608/week-1-july-1st-july-7th/3804/
"""

from typing import List, Dict


class Solution:
    def min_set_size(self, arr: List[int]) -> int:
        # max frequency greedy approach should work here
        # thank you hints
        freq_map = self._compute_freq_map(arr)
        freq_map_keys_sorted = self._sort_freq_map_keys(freq_map)
        half_len = len(arr) / 2
        removed_count = 0
        removed_set_size = 0
        for key in freq_map_keys_sorted:
            removed_count += freq_map[key]
            removed_set_size += 1
            if removed_count >= half_len:
                break

        return removed_set_size


    def _compute_freq_map(self, arr: List[int]) -> Dict[int, int]:
        res = dict()
        for a in arr:
            res[a] = res.get(a, 0) + 1
        return res


    def _sort_freq_map_keys(self, freq_map: Dict[int, int]) -> Dict[int, int]:
        return sorted(freq_map.keys(), key=freq_map.get, reverse=True)
