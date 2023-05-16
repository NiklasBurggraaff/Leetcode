from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1

        currentHeight = min(height[left], height[right])
        count = 0

        while left < right:
            if height[left] > height[right]:
                right -= 1
                h = height[right]
            else:
                left += 1
                h = height[left]

            if h > currentHeight:
                currentHeight = min(height[left], height[right])
            else:
                count += currentHeight - h

        return count


def main():
    print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    print(Solution().trap([4, 2, 0, 3, 2, 5]))


if __name__ == '__main__':
    main()
