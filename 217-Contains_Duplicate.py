from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for zahl in nums:
            if zahl in seen:
                return True
            seen.add(zahl)
        return False