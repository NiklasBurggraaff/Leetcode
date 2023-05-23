class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        res = 0

        chars = set()

        for c in s:
            while c in chars:
                chars.remove(s[left])
                left += 1

            chars.add(c)

            if len(chars) > res:
                res = len(chars)

        return res


def main():
    print(Solution().lengthOfLongestSubstring("abcabcbb"))


if __name__ == "__main__":
    main()
