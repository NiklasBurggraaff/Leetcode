from typing import List


class Solution:
    def soldiersInRow(self, row: List[int]) -> int:
        count = 0
        for x in row:
            if x == 0:
                return count
            count += 1
        return count

    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        n = len(mat)
        soldiers = [self.soldiersInRow(row) for row in mat]

        tuples = [(i, soldiers[i]) for i in range(n)]

        tuples.sort(key=lambda t: t[1])

        return [t[0] for t in tuples[:k]]
