from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        lo, hi = 0, n * m - 1

        while lo <= hi:
            mid = lo + ((hi - lo) // 2)
            num = matrix[mid // m][mid % m]
            if num == target:
                return True
            elif num > target:
                hi = mid - 1
            else:
                lo = mid + 1

        return False


def main():
    print(Solution().searchMatrix(
        matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=3))


if __name__ == "__main__":
    main()
