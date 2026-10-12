# https://leetcode.com/problems/apply-operations-on-array-to-maximize-sum-of-squares/

# Example 1:
# Input: nums = [2,6,5,8], k = 2
# Output: 261
# Explanation: We can do the following operations on the array:
# - Choose i = 0 and j = 3, then change nums[0] to (2 AND 8) = 0 and nums[3] to (2 OR 8) = 10. The resulting array is nums = [0,6,5,10].
# - Choose i = 2 and j = 3, then change nums[2] to (5 AND 10) = 0 and nums[3] to (5 OR 10) = 15. The resulting array is nums = [0,6,0,15].
# We can choose the elements 15 and 6 from the final array. The sum of squares is 152 + 62 = 261.
# It can be shown that this is the maximum value we can get.

from typing import List

class Solution:
    def maxSum(self, A: List[int], k: int) -> int:
        # Count how many numbers have each bit set.
        count = [0] * 35

        for a in A:
            # Check each bit position in the current number.
            for i in range(35):
                if a & (1 << i):
                    # Increment the count if the i-th bit is set.
                    count[i] += 1

        # Store the sum of squares of the k constructed numbers.
        res = 0

        # Modulo value to prevent the result from becoming too large.
        mod = 10 ** 9 + 7

        # Construct k numbers by greedily using available set bits.
        for j in range(k):
            cur = 0

            for i in range(35):
                # If this bit is available, include it in the current number.
                if count[i]:
                    # Use this occurrence of the bit only once.
                    count[i] -= 1

                    # Set the i-th bit in the current number.
                    cur += 1 << i

            # Add the square of the constructed number modulo mod.
            res += cur * cur % mod

        # Return the final result modulo mod.
        return res % mod