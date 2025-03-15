# https://leetcode.com/problems/house-robber-iv/

# Example 1:
# Input: nums = [2,3,5,9], k = 2
# Output: 5
# Explanation: 
# There are three ways to rob at least 2 houses:
# - Rob the houses at indices 0 and 2. Capability is max(nums[0], nums[2]) = 5.
# - Rob the houses at indices 0 and 3. Capability is max(nums[0], nums[3]) = 9.
# - Rob the houses at indices 1 and 3. Capability is max(nums[1], nums[3]) = 9.
# Therefore, we return min(5, 9, 9) = 5.

from typing import List

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        # Function to check if we can steal from at least 'k' houses 
        # while ensuring no two adjacent houses are robbed
        def can_steal_k_houses(capability):
            count = 0  # Number of houses robbed
            i = 0  
            while i < len(nums):
                if nums[i] <= capability:  # If house is within capability limit
                    count += 1  
                    i += 2  # Skip the next house to avoid adjacent robbery
                else:
                    i += 1  # Move to the next house
            return count >= k  # Check if at least 'k' houses were robbed
        
        left, right = min(nums), max(nums)  # Binary search range
        
        # Binary search for the minimum capability needed to rob 'k' houses
        while left < right:
            mid = left + (right - left) // 2  # Mid capability to check
            if can_steal_k_houses(mid):  
                right = mid  # Try to minimize capability
            else:
                left = mid + 1  # Increase capability
        
        return left  # Minimum capability required to rob 'k' houses
