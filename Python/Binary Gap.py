# https://leetcode.com/problems/binary-gap/

# Example 1:
# Input: n = 22
# Output: 2
# Explanation: 22 in binary is "10110".
# The first adjacent pair of 1's is "10110" with a distance of 2.
# The second adjacent pair of 1's is "10110" with a distance of 1.
# The answer is the largest of these two distances, which is 2.
# Note that "10110" is not a valid pair since there is a 1 separating the two 1's underlined.

class Solution:
    def binaryGap(self, n: int) -> int:
        longest_dist = 0   # stores maximum distance between consecutive 1 bits
        i = 0              # current bit position (starting from LSB)
        one_position = 32  # last seen position of '1' (initialized far away)

        # Traverse bits of n from right to left
        while n:
            # Check if current least significant bit is 1
            if n & 1:
                # Update maximum distance between current 1
                # and previous 1 (if larger)
                longest_dist = (
                    i - one_position
                    if i - one_position > longest_dist
                    else longest_dist
                )

                # Update last seen position of 1
                one_position = i

            # Move to next bit
            i += 1
            n >>= 1   # right shift → discard processed bit

        # Return maximum gap between consecutive 1s
        return longest_dist