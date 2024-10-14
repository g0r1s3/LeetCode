from collections import Counter
from typing import List

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # Initialisiere den gemeinsamen Buchstaben-Zähler mit dem ersten Wort
        common_count = Counter(words[0])
        
        # Gehe durch jedes weitere Wort
        for word in words[1:]:
            # Finde den Schnittpunkt der Zählungen mit `&` Operator
            word_count = Counter(word)
            common_count &= word_count  # Erhält die minimalen Häufigkeiten
            
        # Wandle die Buchstaben und deren Häufigkeiten in eine Liste
        common_chars = []
        for letter, count in common_count.items():
            common_chars.extend([letter] * count)
        
        return common_chars