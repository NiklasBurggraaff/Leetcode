from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)

        maxArea = 0
        stack = []

        for i in range(n):
            start = i
            while len(stack) > 0 and heights[i] < stack[-1][1]:
                j, h = stack.pop()
                area = (i - j) * h
                start = j
                if area > maxArea:
                    maxArea = area

            if len(stack) == 0 or heights[i] > stack[-1][1]:
                stack.append((start, heights[i]))

        while len(stack) > 0:
            j, h = stack.pop()
            area = (n - j) * h
            if area > maxArea:
                maxArea = area

        return maxArea


def main():
    print(Solution().largestRectangleArea([3, 6, 5, 7, 4, 8, 1, 0]))


if __name__ == "__main__":
    main()
