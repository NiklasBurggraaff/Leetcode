from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return [""]
        if n == 1:
            return ["()"]

        ret = []

        for firstOpenClosedAfter in range(n):
            betweens = self.generateParenthesis(firstOpenClosedAfter)
            afters = self.generateParenthesis(n - firstOpenClosedAfter - 1)

            for between in betweens:
                for after in afters:
                    ret.append("(" + between + ")" + after)

        return ret


def main():
    for i in range(1, 9):
        print(f"{i}: {Solution().generateParenthesis(i)}")


if __name__ == "__main__":
    main()
