# https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/

# Example 1:
# Input: nums = [2,1,3,4], k = 1
# Output: 2
# Explanation: We can do the following operations:
# - Choose element 2 which is 3 == (011)2, we flip the first bit and we obtain (010)2 == 2. nums becomes [2,1,2,4].
# - Choose element 0 which is 2 == (010)2, we flip the third bit and we obtain (110)2 = 6. nums becomes [6,1,2,4].
# The XOR of elements of the final array is (6 XOR 1 XOR 2 XOR 4) == 1 == k.
# It can be shown that we cannot make the XOR equal to k in less than 2 operations.

from typing import List
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        final_xor = 0
        # XOR of all integers in the array.
        for n in nums:
            final_xor = final_xor ^ n

        count = 0
        # Keep iterating until both k and final_xor becomes zero.
        while k or final_xor:
            # k % 2 returns the rightmost bit in k,
            # final_xor % 2 returns the rightmost bit in final_xor.
            # Increment counter, if the bits don't match.
            if (k % 2) != (final_xor % 2):
                count += 1

            # Remove the last bit from both integers.
            k //= 2
            final_xor //= 2

        return count