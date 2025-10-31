# https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/

# Example 3:
# Input: nums = [7,1,5,4,3,4,6,0,9,5,8,2]
# Output: [4,5]
# Explanation:
# The numbers 4 and 5 each appear twice in the array.

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        """
        Given a list of integers where each number appears once or twice,
        find all the numbers that appear twice (i.e., 'sneaky numbers').

        This uses an in-place marking technique (without extra space)
        by changing the sign of elements to track visited indices.
        """

        n = len(nums)
        
        # Step 1: Increment all numbers by 1 to avoid issues if a number is 0
        # (since array indices start from 0)
        for i in range(n):
            nums[i] += 1

        ans = []  # To store duplicate (sneaky) numbers

        # Step 2: Iterate through each number
        for i in range(n):
            index = abs(nums[i]) - 1  # Get the actual index (convert back after shifting)

            # If nums[index] is negative, it means this index was visited before → duplicate found
            if nums[index] < 0:
                ans.append(index)  # The number (index) appeared twice
            else:
                # Mark this index as visited by making its value negative
                nums[index] *= -1  

        return ans
