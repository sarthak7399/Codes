# https://leetcode.com/problems/max-consecutive-ones-iii/?envType=study-plan-v2&envId=leetcode-75

# Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
# Output: 10
# Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

from typing import List
class Solution:
    def longestOnes(self, A: List[int], k: int) -> int:
      left = right = 0  # Initialize two pointers for the sliding window
      
      for right in range(len(A)):
        if A[right] == 0:   # If we encounter a 0, decrement k
          k -= 1
        # Else, no impact on k
        
        if k < 0:   # If k becomes negative, move the left part of the window to remove extra 0's
          if A[left] == 0:  # If the leftmost element was 0, adjust k
            k += 1
          left += 1 # If we keep seeing 1's, the window still moves as-is
      
      return right - left + 1