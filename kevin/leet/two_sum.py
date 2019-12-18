"""
https://leetcode.com/problems/two-sum/description/
"""


class Solution():
    def two_sum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        Using hashing to solve.
        """
        # Simple cases
        if len(nums) < 2:
            return None
        if len(nums) == 2:
            if nums[0] + nums[1] == target:
                return [0, 1]
            return None

        # Handle case where doubles appear
        hash_dict = {}  # maps value -> list of indices in nums
        double_case = target % 2 == 0
        for index, value in enumerate(nums):
            # Add the current
            current = hash_dict.get(value, [])
            current.append(index)
            hash_dict[value] = current

            # Check backwards
            if double_case and target / 2 in hash_dict and len(hash_dict[target / 2]) > 1:
                return hash_dict[target / 2][: 2]

            # Check others
            if target - value in hash_dict and hash_dict[target - value] != hash_dict[value]:
                return [hash_dict[value][0], hash_dict[target - value][0]]
