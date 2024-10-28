class Solution:
    def addDigits(self, num: int) -> int:
        laufnummer = num
        while laufnummer > 9:
            laufnummer = self.quersumme(laufnummer)
        return laufnummer
        
    def quersumme(self, n: int) -> int:
        return sum(int(digit) for digit in str(n))