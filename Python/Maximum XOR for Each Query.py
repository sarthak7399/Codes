# https://leetcode.com/problems/maximum-xor-for-each-query/

# Example 1:
# Input: nums = [0,1,1,3], maximumBit = 2
# Output: [0,3,2,3]
# Explanation: The queries are answered as follows:
# 1st query: nums = [0,1,1,3], k = 0 since 0 XOR 1 XOR 1 XOR 3 XOR 0 = 3.
# 2nd query: nums = [0,1,1], k = 3 since 0 XOR 1 XOR 1 XOR 3 = 3.
# 3rd query: nums = [0,1], k = 2 since 0 XOR 1 XOR 2 = 3.
# 4th query: nums = [0], k = 3 since 0 XOR 3 = 3.

from typing import List
class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        # Step 1: Initialize necessary variables
        n = len(nums)  # Length of the input list 'nums'
        
        # Calculate the maximum XOR value for any number within the specified bit limit
        # For example, if maximumBit is 3, max_xor will be 7 (binary '111')
        max_xor = (1 << maximumBit) - 1

        # Step 2: Compute the cumulative XOR of all numbers in 'nums'
        # This will help us get the XOR of the entire array initially
        xorr = nums[0]
        for i in range(1, n):
            xorr ^= nums[i]  # XOR each element in the array with the cumulative XOR
        
        # Step 3: Prepare to collect the results in reverse order
        ans = []
        for i in range(n):
            # XOR 'xorr' with 'max_xor' to find the maximum possible XOR for the current configuration
            ans.append(xorr ^ max_xor)
            
            # Update 'xorr' by removing the last element's effect from the cumulative XOR
            # 'n - 1 - i' accesses elements from the end of the list in each iteration
            xorr ^= nums[n - 1 - i]
        
        return ans
