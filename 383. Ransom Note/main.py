class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counts = {}

        for magChar in magazine:
            if magChar not in counts:
                counts[magChar] = 1
            else:
                counts[magChar] += 1

        for noteChar in ransomNote:
            if noteChar not in counts or counts[noteChar] <= 0:
                return False

            counts[noteChar] -= 1

        return True


def main():
    print("ransomNote = \"a\", magazine = \"b\": " +
          str(Solution().canConstruct("a", "b")))
    print("ransomNote = \"aa\", magazine = \"ab\": " +
          str(Solution().canConstruct("aa", "ab")))
    print("ransomNote = \"aa\", magazine = \"aab\": " +
          str(Solution().canConstruct("aa", "aab")))


if __name__ == "__main__":
    main()
