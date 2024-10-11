class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        pos = 0  # Position für das nächste Nicht-Null-Element
        for number in nums:
            if number != 0:
                nums[pos] = number
                pos += 1
        # Fülle die restlichen Positionen mit Nullen
        for i in range(pos, len(nums)):
            nums[i] = 0