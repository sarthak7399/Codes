# https://leetcode.com/problems/minimum-array-end/

# Example 1:
# Input: n = 3, x = 4
# Output: 6
# Explanation:
# nums can be [4,5,6] and its last element is 6.

class Solution:
    def minEnd(self, n: int, x: int) -> int:
        # Initialize 'result' to 'x' as the starting point for the final result.
        result = x

        # 'remaining' holds the count of bits needed to reach 'n - 1'
        # (i.e., the binary representation of n - 1)
        remaining = n - 1

        # 'position' keeps track of the current bit position we're examining (starting with 1, the least significant bit).
        position = 1
    
        # Continue the loop until there are no more bits left in 'remaining' to process.
        while remaining:
            # Check if the current bit in 'x' at 'position' is not set (i.e., equals 0).
            if not (x & position):
                # If the bit is not set, add the corresponding bit from 'remaining' to 'result' at this 'position'.
                result |= (remaining & 1) * position  # Set the bit in 'result' if the current bit in 'remaining' is 1.
                
                # Right-shift 'remaining' by 1 to move to the next bit.
                remaining >>= 1
            
            # Move to the next bit position by left-shifting 'position'.
            position <<= 1
    
        # Return the final result, which now represents the modified number.
        return result
