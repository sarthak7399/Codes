# https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/

# Example 1:
# Input: n = 5
# Output: [-7,-1,1,3,4]
# Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].

from typing import List

class Solution:
    def sumZero(self, n: int) -> List[int]:
        # Initialize an array of length n with all 0s
        arr = [0] * n  
        k = 1  # Start with positive integer 1

        # Fill the array symmetrically from both ends
        # Each pair (k, -k) will cancel out, keeping the total sum = 0
        for i in range(n // 2):
            arr[i] = k              # Place positive number on the left side
            arr[n - 1 - i] = -k     # Place its negative counterpart on the right side
            k += 1                  # Move to the next integer

        # If n is odd, the middle element will remain 0 (from initialization),
        # so the overall sum is still guaranteed to be 0.
        return arr
