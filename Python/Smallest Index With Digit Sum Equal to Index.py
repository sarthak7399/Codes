# https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/

# Example 1:
# Input: nums = [1,3,2]
# Output: 2
# Explanation:
# For nums[2] = 2, the sum of digits is 2, which is equal to index i = 2. Thus, the output is 2.

class Solution:
    def smallestIndex(self, nums):

        # Check each index in the array.
        for i in range(len(nums)):
            # Store the current number.
            x = nums[i]

            # Store the sum of digits of the current number.
            total = 0

            # Calculate the sum of digits.
            while x > 0:
                # Add the last digit to the sum.
                total += x % 10

                # Remove the last digit.
                x //= 10

            # If the digit sum equals the current index,
            # return this index.
            if total == i:
                return i

        # Return -1 if no such index exists.
        return -1