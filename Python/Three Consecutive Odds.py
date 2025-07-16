# https://leetcode.com/problems/three-consecutive-odds/

# Example 1:
# Input: arr = [2,6,4,1]
# Output: false
# Explanation: There are no three consecutive odds.

from typing import List

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        i = 0
        # Iterate through the array up to the third-last element
        while(i < len(arr) - 2):
            # Check if the current element and the next two elements are all odd
            if (arr[i] % 2 != 0) and (arr[i + 1] % 2 != 0) and (arr[i + 2] % 2 != 0):
                return True  # Found three consecutive odd numbers
            i += 1  # Move to the next element
        return False  # No three consecutive odd numbers found
