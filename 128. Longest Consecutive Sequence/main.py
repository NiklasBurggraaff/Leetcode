from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        sequenceStarts = {}  # key: start number, value: length
        sequenceEnds = {}  # key: end number, value: length

        for x in set(nums):
            before = (x + 1) in sequenceStarts
            after = (x - 1) in sequenceEnds

            if before and after:
                start = x - sequenceEnds[x - 1]
                end = x + sequenceStarts[x + 1]
                length = end - start + 1

                sequenceStarts.pop(x + 1)
                sequenceEnds.pop(x - 1)

                sequenceStarts[start] = length
                sequenceEnds[end] = length
            elif before:
                end = x + sequenceStarts[x + 1]
                length = end - x + 1

                sequenceStarts.pop(x + 1)
                sequenceStarts[x] = length
                sequenceEnds[end] = length
            elif after:
                start = x - sequenceEnds[x - 1]
                length = x - start + 1

                sequenceEnds.pop(x - 1)
                sequenceStarts[start] = length
                sequenceEnds[x] = length
            else:
                sequenceStarts[x] = 1
                sequenceEnds[x] = 1

        return max(sequenceStarts.values())


def main():
    print(Solution().longestConsecutive([100, 4, 200, 1, 3, 2]))
    print(Solution().longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))


if __name__ == "__main__":
    main()
