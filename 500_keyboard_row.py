from typing import List

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        listOfLetters = ["qwertyuiopQWERTYUIOP", "asdfghjklASDFGHJKL", "zxcvbnmZXCVBNM"]
        listOfWordsToReturn = []
        
        for word in words:
            for row in listOfLetters:
                if all(letter in row for letter in word):  # Prüft, ob alle Buchstaben in einer Zeile sind
                    listOfWordsToReturn.append(word)
                    break  # Kein weiteres Überprüfen nötig, wenn das Wort passt
                
        return listOfWordsToReturn

# Testen
s = Solution()
print(s.findWords(["Hello", "Alaska", "Dad", "Peace"]))
