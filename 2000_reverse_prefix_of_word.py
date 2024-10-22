class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch in word:
            parts = word.split(ch, 1)
            parts[0] = parts[0] + ch
            parts[0] = parts[0][::-1]
            return "".join(parts)
        else:
            return word