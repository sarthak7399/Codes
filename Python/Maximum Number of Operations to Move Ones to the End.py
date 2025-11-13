# https://leetcode.com/problems/maximum-number-of-operations-to-move-ones-to-the-end/

# Example 1:
# Input: s = "1001101"
# Output: 4
# Explanation:
# We can perform the following operations:
# Choose index i = 0. The resulting string is s = "0011101".
# Choose index i = 4. The resulting string is s = "0011011".
# Choose index i = 3. The resulting string is s = "0010111".
# Choose index i = 2. The resulting string is s = "0001111".

class Solution:
    def maxOperations(self, s: str) -> int:
        counted_ones = 0   # Tracks number of '1's seen so far
        operations = 0     # Total number of operations

        for i, ch in enumerate(s):
            if ch == "1":
                counted_ones += 1
            else:
                # When '0' follows a '1' or is at the start, count valid operations
                if i == 0 or s[i - 1] == "1":
                    operations += counted_ones

        return operations
        
