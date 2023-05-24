from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1

        while lo < hi:
            i = (hi + lo) // 2

            if nums[i] < nums[i - 1]:
                return nums[i]

            if nums[i] < nums[-1]:
                hi = i - 1
            else:
                lo = i + 1

        if lo >= len(nums):
            return nums[-1]

        return nums[lo]
