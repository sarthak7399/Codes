# https://leetcode.com/problems/keep-multiplying-found-values-by-two/

# Example 1:
# Input: nums = [5,3,6,1,12], original = 3
# Output: 24
# Explanation: 
# - 3 is found in nums. 3 is multiplied by 2 to obtain 6.
# - 6 is found in nums. 6 is multiplied by 2 to obtain 12.
# - 12 is found in nums. 12 is multiplied by 2 to obtain 24.
# - 24 is not found in nums. Thus, 24 is returned.

class Solution:
    def findFinalValue(self, nums: list[int], k: int) -> int:
        bits = 0

        # Check every number in the list
        for num in nums:
            q, r = divmod(num, k)   # q = num // k, r = num % k

            # Valid only if divisible by k and quotient is power of 2
            if r == 0 and (q & (q - 1)) == 0:
                bits |= q           # Record this power of two in bitmask

        # Next missing power of two after all seen ones
        n = bits + 1

        # Return k multiplied by lowest set bit in n
        return k * (n & -n)
