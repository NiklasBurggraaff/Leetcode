class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        minVal = self.getMin()
        if minVal is None or val <= minVal:
            self.minStack.append(val)

    def pop(self) -> None:
        if len(self.minStack) > 0 and self.top() == self.getMin():
            self.minStack.pop()

        self.stack.pop()

    def top(self) -> int:
        if not self.stack:
            return None

        return self.stack[-1]

    def getMin(self) -> int:
        if not self.minStack:
            return None

        return self.minStack[-1]


def main():
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin(), -3)
    minStack.pop()
    print(minStack.top(), 0)
    print(minStack.getMin(), -2)


if __name__ == "__main__":
    main()
