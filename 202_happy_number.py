class Solution:
    def isHappy(self, n: int) -> bool:
        runner = n
        for i in range(500):
            runner = (self.quadratQuersumme(runner))
            if runner == 1:
                return True
        return False

    def quadratQuersumme(self, n: int) -> int:
        summe = 0
        for i in str(n):
            summe = summe + int(i)*int(i)
        return summe