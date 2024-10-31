class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        neccessaryLetters = list(ransomNote)
        availableLetters = list(magazine)
        for letter in availableLetters:
            if letter in neccessaryLetters:
                neccessaryLetters.remove(letter)
        if(len(neccessaryLetters) == 0):
            return True
        else:
            return False