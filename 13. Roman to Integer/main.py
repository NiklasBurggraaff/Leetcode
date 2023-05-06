symbolValues = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}


class Solution:
    def romanToInt(self, s: str) -> int:
        value = 0

        prevChar = None
        prevCharCount = 0
        prevCharVal = None

        for c in s:
            cVal = symbolValues[c]

            if prevCharVal is None:
                prevChar = c
                prevCharCount = 1
                prevCharVal = cVal
                continue

            if c == prevChar:
                prevCharCount += 1
                continue

            if cVal > prevCharVal:
                value -= prevCharVal * prevCharCount
            else:
                value += prevCharVal * prevCharCount

            prevChar = c
            prevCharCount = 1
            prevCharVal = cVal

        value += prevCharVal * prevCharCount

        return value


def main():
    print("III: " + str(Solution().romanToInt("III")))
    print("LVIII: " + str(Solution().romanToInt("LVIII")))


if __name__ == "__main__":
    main()
