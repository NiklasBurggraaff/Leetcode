from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numberStack = []

        for t in tokens:
            if t == "+":
                numberStack.append(numberStack.pop() + numberStack.pop())
            elif t == "-":
                temp = numberStack.pop()
                numberStack.append(numberStack.pop() - temp)
            elif t == "*":
                numberStack.append(numberStack.pop() * numberStack.pop())
            elif t == "/":
                temp = numberStack.pop()
                numberStack.append(int(numberStack.pop() / temp))
            else:
                numberStack.append(int(t))

        return numberStack[0]


def main():
    print(Solution().evalRPN(["2", "1", "+", "3", "*"]), 9)
    print(Solution().evalRPN(["4", "13", "5", "/", "+"]), 6)
    print(Solution().evalRPN(["10", "6", "9", "3", "+",
          "-11", "*", "/", "*", "17", "+", "5", "+"]), 22)


if __name__ == "__main__":
    main()
