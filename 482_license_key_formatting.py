class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        # Schritt 1 und 2: Entferne Bindestriche und konvertiere in Großbuchstaben
        s = s.replace('-', '').upper()
        
        # Schritt 3 und 4: Teile den String in Gruppen von k Zeichen von rechts
        result = []
        while len(s) > k:
            result.append(s[-k:])  # Nimm die letzten k Zeichen
            s = s[:-k]             # Entferne die letzten k Zeichen aus s
        
        # Füge den restlichen (oder ersten) Teil hinzu
        result.append(s)
        
        # Schritt 5: Verbinde die Gruppen mit Bindestrichen
        return '-'.join(result[::-1])  # Von hinten nach vorne zusammenfügen