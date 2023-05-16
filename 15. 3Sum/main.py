from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []

        for i in range(len(nums) - 2):
            x = nums[i]
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:
                sum = x + nums[left] + nums[right]
                if sum == 0:
                    res.append([x, nums[left], nums[right]])

                    left += 1
                    right -= 1

                    while left < right and nums[left - 1] == nums[left]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                    continue

                if sum > 0:
                    right -= 1
                else:
                    left += 1

        return res


def main():
    print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
    print(Solution().threeSum([0, 1, 1]))
    print(Solution().threeSum([0, 0, 0]))


if __name__ == "__main__":
    main()
