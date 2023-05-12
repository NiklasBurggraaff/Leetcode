from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remainders = dict()

        for i in range(len(nums)):
            x = nums[i]

            if x in remainders:
                return [remainders[x], i]

            remainders[target - x] = i
