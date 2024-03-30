# https://leetcode.com/problems/number-of-1-bits/description/?envType=daily-question&envId=2024-03-10

# Example 1:
# Input: n = 00000000000000000000000000001011
# Output: 3
# Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0  # Initialize a variable to count the number of bits set to 1
        while n:  # Continue the loop until n becomes zero
            count += n & 1  # Add 1 to count if the least significant bit of n is 1
            n >>= 1  # Right shift n by one position to check the next bit
        return count  # Return the count of bits set to 1 (Hamming weight)
