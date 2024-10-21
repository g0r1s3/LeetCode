from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = []
        sum = 0
        for operation in operations:
            if operation not in ("+", "D", "C"):
                score.append(operation)
            if operation == "D":
                score.append(int(score[-1])*2)
            if operation == "C":
                score.pop()
            if operation == "+":
                score.append(int(score[-1])+int(score[-2]))
        for element in score:
            sum = sum + int(element)
        return sum 

solution = Solution()
print(solution.calPoints(["5", "2", "C", "D", "+"]))
