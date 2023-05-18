class Solution:
    def isValid(self, s: str) -> bool:
        open = "([{"
        closed = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if c in open:
                stack.append(c)
            elif c in closed:
                if len(stack) > 0 and stack[-1] == closed[c]:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0


def main():
    print(Solution().isValid("()"))
    print(Solution().isValid("()[]{}"))
    print(Solution().isValid("(]"))


if __name__ == "__main__":
    main()
