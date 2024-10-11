class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching_bracket = {')': '(', ']': '[', '}': '{'}
        
        for char in s:
            if char in matching_bracket.values():  # öffnende Klammern
                stack.append(char)
            elif char in matching_bracket:  # schließende Klammern
                if not stack or stack[-1] != matching_bracket[char]:
                    return False
                stack.pop()  # Klammerpaar korrekt, also schließende entfernen
            else:
                return False  # Ungültiges Zeichen
        
        return not stack  # Stack muss leer sein, wenn alle Klammern korrekt geschlossen wurden
