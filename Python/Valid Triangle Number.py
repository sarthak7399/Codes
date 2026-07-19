# https://leetcode.com/problems/valid-triangle-number/

# Example 1:
# Input: nums = [2,2,3,4]
# Output: 3
# Explanation: Valid combinations are: 
# 2,3,4 (using the first 2)
# 2,3,4 (using the second 2)
# 2,2,3

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()              # Sort the numbers
        n = len(nums)
        count = 0

        for i in range(n - 1, -1, -1):   # Pick the largest side as nums[i]
            left, right = 0, i - 1       # Use two-pointer approach on the rest
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    count += right - left
                    right -= 1
                else:
                    left += 1
        return count
