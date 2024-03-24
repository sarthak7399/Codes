# https://leetcode.com/problems/find-the-duplicate-number/description/?envType=daily-question&envId=2024-03-15

# Example 1:
# Input: nums = [1,3,4,2,2]
# Output: 2

from typing import List
# # Method 1 - Time Complexity O(N), Space Complexity O(N)
# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
#         hashmap = {}
#         for i in nums:
#             if i in hashmap:
#                 return i
#             hashmap[i] = 1
#         return -1
    
# Method 2 - Time Complexity O(N), Space Complexity O(1)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Phase 1: Detect if there is a cycle
        slow = nums[0]
        fast = nums[0]
        
        # Move slow pointer one step and fast pointer two steps
        while True:
            slow = nums[slow]  # Move one step
            fast = nums[nums[fast]]  # Move two steps
            
            if slow == fast:
                break  # Cycle detected
        
        # Phase 2: Find the start of the cycle (Duplicate number)
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow  # Return the duplicate number
