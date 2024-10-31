class Solution:
    def firstUniqChar(self, s: str) -> int:
        haeufigkeit = {}

        for buchstabe in s:
            if buchstabe in haeufigkeit:
                haeufigkeit[buchstabe] += 1
            else:
                haeufigkeit[buchstabe] = 1

        index = -1
        for i, buchstabe in enumerate(s):
            if haeufigkeit[buchstabe] == 1:
                index = i
                break
        return index