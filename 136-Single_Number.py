class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ergebnis = 0
        for zahl in nums:
            ergebnis ^= zahl
        return ergebnis
            