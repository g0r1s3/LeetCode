from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = int("".join(map(str, digits)))
        number += 1
        numberPlusOne = [int(char) for char in str(number)]
        return numberPlusOne