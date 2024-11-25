from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dictionary to store the numbers and their indices
        num_to_index = {}

        # Iterate through the array
        for i, num in enumerate(nums):
            # Calculate the complement that would add up to the target
            complement = target - num

            # Check if the complement exists in the dictionary
            if complement in num_to_index:
                # Return the indices of the two numbers
                return [num_to_index[complement], i]

            # Store the number and its index in the dictionary
            num_to_index[num] = i

        # If no solution is found, return an empty list (though it shouldn't happen based on the problem statement)
        return []