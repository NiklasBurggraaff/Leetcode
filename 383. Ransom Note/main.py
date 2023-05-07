from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        noteCounter = Counter(ransomNote)
        magazineCounter = Counter(magazine)

        for char in noteCounter:
            if char not in magazineCounter:
                return False
            if noteCounter[char] > magazineCounter[char]:
                return False

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
