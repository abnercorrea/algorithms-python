from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}

        for i in range(len(nums)):
            if target - nums[i] in num_map:
                return [i, num_map[target - nums[i]]]

            num_map[nums[i]] = i
