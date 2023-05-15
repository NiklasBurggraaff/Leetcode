class Solution:
    def encode(self, strs):
        """
        @param: strs: a list of strings
        @return: encodes a list of strings to a single string.
        """
        if strs == []:
            return ""

        str = ""

        for s in strs:
            str += ":;"
            str += s.replace(":", "::")

        return str

    def decode(self, str):
        """
        @param: str: A string
        @return: decodes a single string to a list of strings
        """
        if str == "":
            return []

        strs = []
        i = -1

        specialChar = False
        for char in str:
            if specialChar:
                specialChar = False
                if char == ";":
                    i += 1
                    strs.append("")
                    continue
            elif char == ":":
                specialChar = True
                continue

            if i >= 0:
                strs[i] += char

        return strs


def main():
    encoding = Solution().encode(["lint", "code", "love", "you"])
    print("Encoding: " + encoding)
    print(["lint", "code", "love", "you"], Solution().decode(encoding))

    encoding = Solution().encode(["lint", "code", "love", ":", "you"])
    print("Encoding: " + encoding)
    print(["lint", "code", "love", ":", "you"], Solution().decode(encoding))

    encoding = Solution().encode([""])
    print("Encoding: " + encoding)
    print([""], Solution().decode(encoding))

    encoding = Solution().encode([])
    print("Encoding: " + encoding)
    print([], Solution().decode(encoding))

    encoding = Solution().encode(["lint", "code", "love", "you", ""])
    print("Encoding: " + encoding)
    print(["lint", "code", "love", "you", ""], Solution().decode(encoding))


if __name__ == '__main__':
    main()
