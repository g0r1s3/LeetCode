class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        listOfWords = sentence.split()
        for i, word in enumerate(listOfWords):
            if word.startswith(("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")):
                listOfWords[i] = word + "ma"
            if not word.startswith(("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")):
                # Buchstaben am anfang speichern
                firstChar = word[0]
                listOfWords[i] = word[1:] + firstChar + "ma"
            # Für jeden Buchstaben ein a am ende + 1
            aCounter = i + 1
            while aCounter > 0:
                listOfWords[i] = listOfWords[i] + "a"
                aCounter = aCounter -1
        return " ".join(listOfWords)
    