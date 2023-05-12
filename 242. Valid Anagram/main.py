class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        a = ord('a')

        counts = [0] * 26

        for c in s:
            counts[ord(c) - a] += 1

        for c in t:
            i = ord(c) - a
            if counts[i] == 0:
                return False

            counts[i] -= 1

        return True
