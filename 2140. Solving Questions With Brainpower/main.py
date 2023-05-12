from typing import List


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            if i + questions[i][1] + 1 >= n:
                dp[i] = max(questions[i][0], dp[i + 1])
            else:
                dp[i] = max(questions[i][0] + dp[i + questions[i][1] + 1],
                            dp[i + 1])

        return dp[0]


def main():
    print(Solution().mostPoints([[3, 2], [4, 3], [4, 4], [2, 5]]))
    print(Solution().mostPoints([[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]))


if __name__ == "__main__":
    main()
