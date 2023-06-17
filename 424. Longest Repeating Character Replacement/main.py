class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        l = 0

        res = 0
        maxf = 0
        for r in range(len(s)):
            counts[s[r]] = 1 + counts.get(s[r], 0)
            if counts[s[r]] > maxf:
                maxf = counts[s[r]]

            while (r - l + 1) - maxf > k:
                counts[s[l]] -= 1
                l += 1

            if (r - l + 1) > res:
                res = r - l + 1

        return res


def main():
    print(Solution().characterReplacement("ABAB", 2))
    print(Solution().characterReplacement("AABABBA", 1))
    print(Solution().characterReplacement("AAAA", 2))
    print(Solution().characterReplacement("BAAAB", 2))


if __name__ == "__main__":
    main()
