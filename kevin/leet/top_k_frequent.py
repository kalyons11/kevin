# https://leetcode.com/problems/top-k-frequent-elements/

class Solution:

    def top_k_frequent(self, nums, k):
        # Given a non-empty array of integers, return the k most frequent
        # elements.

        # 1. Construct frequency dictionary
        freq = self.__freq_dict(nums)

        # 2. Sort keys by values descending
        top_keys = sorted(freq.keys(), key=lambda k: freq[k], reverse=True)

        # 3. Return top k, sorted
        return sorted(list(top_keys)[:k])

    def __freq_dict(self, nums):
        # Returns a dictionary mapping unique values of nums to number of
        # occurances in nums
        result = dict()
        for num in nums:
            result[num] = result.get(num, 0) + 1

        return result
