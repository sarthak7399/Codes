# https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/

# Example 1:
# Input: blocks = "WBBWWBBWBW", k = 7
# Output: 3
# Explanation:
# One way to achieve 7 consecutive black blocks is to recolor the 0th, 3rd, and 4th blocks
# so that blocks = "BBBBBBBWBW". 
# It can be shown that there is no way to achieve 7 consecutive black blocks in less than 3 operations.
# Therefore, we return 3.

class Solution:
    def minimumRecolors(self, s: str, k: int) -> int:
        n = len(s)
        w = sum(1 for i in range(k) if s[i] == "W")  # Count 'W' in the first window of size k
        minw = w  # Initialize the minimum 'W' count

        # Slide the window across the string
        for i in range(k, n):
            if s[i] == "W":  
                w += 1  # Add new 'W' entering the window
            if s[i - k] == "W":  
                w -= 1  # Remove 'W' leaving the window
            minw = min(minw, w)  # Update minimum 'W' count
        
        return minw  # Return the minimum 'W' count in any window of size k
