class Solution:
    def isPalindrome(self, s: str) -> bool:
        special_characters = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ "
        cleanS = s.lower()
        for char in special_characters:
            cleanS = cleanS.replace(char, "")
        return cleanS == cleanS[::-1]

s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))