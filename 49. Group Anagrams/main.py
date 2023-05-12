import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret = collections.defaultdict(list)

        for str in strs:
            counts = [0] * 26

            for c in str:
                counts[ord(c) - ord("a")] += 1

            index = tuple(counts)

            ret[index].append(str)

        return ret.values()
