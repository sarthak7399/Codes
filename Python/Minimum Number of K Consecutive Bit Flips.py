# https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/

# Example 3:
# Input: nums = [0,0,0,1,0,1,1,0], k = 3
# Output: 3
# Explanation: 
# Flip nums[0],nums[1],nums[2]: nums becomes [1,1,1,1,0,1,1,0]
# Flip nums[4],nums[5],nums[6]: nums becomes [1,1,1,1,1,0,0,0]
# Flip nums[5],nums[6],nums[7]: nums becomes [1,1,1,1,1,1,1,1]

from typing import List
class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        n = len(A)
        flipped_count = 0  # Tracks the cumulative number of flips at each position
        flip_operations = 0  # Total number of flips performed
        flip_flags = [0] * n  # Tracks flip operations that impact each position
        
        for i in range(n):
            # If we are beyond the first K elements, we need to remove the effect of the oldest flip
            if i >= K:
                flipped_count ^= flip_flags[i - K]
            
            # If the current bit is not as desired (0 instead of 1), we need to flip
            if flipped_count == A[i]:
                # If there's not enough space to flip K bits, return -1
                if i + K > n:
                    return -1
                flip_flags[i] = 1
                flipped_count ^= 1  # Update the cumulative flip count
                flip_operations += 1
        
        return flip_operations
