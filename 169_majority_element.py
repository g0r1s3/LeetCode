from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elements = {}
        max = 0
        # durchlaufe die liste und füge jedes einzelne Element zu elements hinzu
        for num in nums:
            if (num in elements):
                elements[num] += 1
            else:
                elements[num] = 1
        # jetzt Wert mit höchstem Value herausfinden
        for element in elements:
            if(elements[element] > max):
                max = elements[element]
        for key, value in elements.items():
            if value == max:
                return key