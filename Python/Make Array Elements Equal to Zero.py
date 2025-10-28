# https://leetcode.com/problems/make-array-elements-equal-to-zero/

# Example 1:
# Input: nums = [1,0,2,0,3]
# Output: 2
# Explanation:
# The only possible valid selections are the following:
# Choose curr = 3, and a movement direction to the left.
# [1,0,2,0,3] -> [1,0,2,0,3] -> [1,0,1,0,3] -> [1,0,1,0,3] -> [1,0,1,0,2] -> [1,0,1,0,2] -> [1,0,0,0,2] -> [1,0,0,0,2] -> [1,0,0,0,1] -> [1,0,0,0,1] -> [1,0,0,0,1] -> [1,0,0,0,1] -> [0,0,0,0,1] -> [0,0,0,0,1] -> [0,0,0,0,1] -> [0,0,0,0,1] -> [0,0,0,0,0].
# Choose curr = 3, and a movement direction to the right.
# [1,0,2,0,3] -> [1,0,2,0,3] -> [1,0,2,0,2] -> [1,0,2,0,2] -> [1,0,1,0,2] -> [1,0,1,0,2] -> [1,0,1,0,1] -> [1,0,1,0,1] -> [1,0,0,0,1] -> [1,0,0,0,1] -> [1,0,0,0,0] -> [1,0,0,0,0] -> [1,0,0,0,0] -> [1,0,0,0,0] -> [0,0,0,0,0].

class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        """
        Counts the number of valid selections in the array `nums`.
        
        A "valid selection" occurs at positions where the number of elements 
        on the left and right (in terms of cumulative sum) satisfy specific 
        balance conditions:
          - If the current element is 0 and left sum == right sum → +2 ways
          - If the current element is 0 and |left - right| == 1 → +1 way
        """

        length = len(nums)
        count = 0        # To store total number of valid selections
        left = 0         # Cumulative sum of elements to the left
        right = sum(nums)  # Cumulative sum of elements to the right

        for i in range(length):
            # Move current element from right sum to left sum
            left += nums[i]
            right -= nums[i]

            # Skip if current element is not 0, since only zeros are considered
            if nums[i] != 0:
                continue

            # Check if left and right sums are equal
            if left == right:
                count += 2  # Two possible ways to balance

            # Check if left and right differ by exactly 1
            if abs(left - right) == 1:
                count += 1  # One possible way to balance

        return count
