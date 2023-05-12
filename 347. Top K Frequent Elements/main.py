from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        freq = [[] for _ in range(len(nums) + 1)]

        for c, n in counts.items():
            freq[n].append(c)

        ret = []
        for i in range(len(freq) - 1, -1, -1):
            for n in freq[i]:
                ret.append(n)

            if (len(ret) == k):
                break

        return ret
