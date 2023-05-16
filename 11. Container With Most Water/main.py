from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1

        maxWater = 0

        while left < right:
            water = (right - left) * min(height[left], height[right])

            if water > maxWater:
                maxWater = water

            if height[right] < height[left]:
                right -= 1
            else:
                left += 1

        return maxWater


def main():
    print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    print(Solution().maxArea([1, 1]))
    print(Solution().maxArea([2, 3, 4, 5, 18, 17, 6]))


if __name__ == "__main__":
    main()
