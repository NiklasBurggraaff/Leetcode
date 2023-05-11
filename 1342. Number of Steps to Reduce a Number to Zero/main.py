from collections import Counter


class SolutionSimple:
    def numberOfSteps(self, num: int) -> int:
        steps = 0

        while num != 0:
            if num % 2 == 0:
                num /= 2
            else:
                num -= 1

            steps += 1

        return steps


class Solution:
    def numberOfSteps(self, num: int) -> int:
        binary = "{0:b}".format(num)

        divisions = len(binary) - 1
        subtractions = binary.count("1")

        return divisions + subtractions


# 10101 -> 10100 -> 1010 -> 101 -> 100 -> 10 -> 1 -> 0
#       Sub      Div     Div    Sub    Div   Div  Sub
# 3x Sub (3x 1)
# 4x Div (Max 1 at pos 4)
