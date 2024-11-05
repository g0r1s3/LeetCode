class Solution:
    def checkRecord(self, s: str) -> bool:
        return 2 > s.count("A") and not("LLL" in s)
    
s = Solution()
print(s.checkRecord("PPALLP"))