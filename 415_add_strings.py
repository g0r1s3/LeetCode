class Solution:
    def addStrings(self, num1, num2):
        # Initialisiere Variablen
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        result = []

        # Gehe durch beide Strings von rechts nach links
        while i >= 0 or j >= 0 or carry:
            digit1 = int(num1[i]) if i >= 0 else 0
            digit2 = int(num2[j]) if j >= 0 else 0

            # Berechne die Summe der aktuellen Stellen und den Übertrag
            total = digit1 + digit2 + carry
            carry = total // 10
            result.append(str(total % 10))

            # Gehe zu den nächsten Ziffern über
            i -= 1
            j -= 1

        # Da das Ergebnis rückwärts aufgebaut wurde, drehe es um
        return ''.join(result[::-1])