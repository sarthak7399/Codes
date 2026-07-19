# https://leetcode.com/problems/largest-perimeter-triangle/

# Example 2:
# Input: nums = [1,2,1,10]
# Output: 0
# Explanation: 
# You cannot use the side lengths 1, 1, and 2 to form a triangle.
# You cannot use the side lengths 1, 1, and 10 to form a triangle.
# You cannot use the side lengths 1, 2, and 10 to form a triangle.
# As we cannot use any three side lengths to form a triangle of non-zero area, we return 0.

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        
        for i in range(n - 1, 1, -1):   # Start from largest side
            a, b, c = nums[i-2], nums[i-1], nums[i]
            if a + b > c:              # Triangle condition
                return a + b + c       # Found largest perimeter
        return 0                       # No valid triangle
