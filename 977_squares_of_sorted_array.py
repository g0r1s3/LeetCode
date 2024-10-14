from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        retList = []
        for num in nums:
            retList.append(num*num)
        retList.sort()
        return retList

solution = Solution()
print(solution.sortedSquares([1,-22,3,4,-5]))