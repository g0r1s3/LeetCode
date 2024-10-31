from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answerList = []
        for i in range(n):
            if (i+1) % 3 == 0 and (i+1) % 5 == 0:
                answerList.append("FizzBuzz")
            elif (i+1) % 3 == 0:
                answerList.append("Fizz")
            elif (i+1) % 5 == 0:
                answerList.append("Buzz")
            else:
                answerList.append(str(i+1))
        return answerList

s = Solution()
print(s.fizzBuzz(15))