import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)

        while lo < hi:
            k = lo + ((hi - lo) // 2)

            time = 0
            for p in piles:
                time += math.ceil(p / k)
                if time > h:
                    break

            if time > h:
                lo = k + 1
            else:
                hi = k

        return lo


def main():
    print(Solution().minEatingSpeed(piles=[3, 6, 7, 11], h=8))


if __name__ == "__main__":
    main()
