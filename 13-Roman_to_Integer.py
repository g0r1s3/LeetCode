class Solution:
    def romanToInt(self, s: str) -> int:
        romanDic = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        result = 0
        # Iteriere über alle Buchstaben der Zeichenkette
        for i in range(len(s)):
            # Überprüfen, ob der aktuelle Wert kleiner als der nächste ist
            if i + 1 < len(s) and romanDic[s[i]] < romanDic[s[i + 1]]:
                result -= romanDic[s[i]]
            else:
                result += romanDic[s[i]]
        
        return result
