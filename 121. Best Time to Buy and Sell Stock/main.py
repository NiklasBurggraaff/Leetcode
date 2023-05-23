from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        minPrice = prices[0]

        for p in prices:
            if p < minPrice:
                minPrice = p
                continue

            profit = p - minPrice
            if profit > res:
                res = profit

        return res


def main():
    print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))


if __name__ == "__main__":
    main()
