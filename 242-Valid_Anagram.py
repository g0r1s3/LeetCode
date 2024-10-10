class Solution:
    def isAnagram(self, s: str, t:str) -> bool:
        if len(s) == len(t):
            firstLetters = []
            for letter in s:
                firstLetters.append(letter)
            for letter in t:
                if letter in firstLetters:
                    firstLetters.remove(letter)
            if firstLetters == []:
                return True
        else:
            return False