# https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/

# Example 1:
# Input: nums = [1,2,3,4]
# Output: 3
# Explanation:
# All array elements can be made divisible by 3 using 3 operations:
# Subtract 1 from 1.
# Add 1 to 2.
# Subtract 1 from 4.

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # Count how many numbers are NOT already divisible by 3
        # Each such number needs one operation
        return sum(num % 3 > 0 for num in nums)
