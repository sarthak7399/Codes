# https://leetcode.com/problems/smallest-missing-multiple-of-k/

# Example 1:
# Input: nums = [8,2,3,4,6], k = 2
# Output: 10
# Explanation:
# The multiples of k = 2 are 2, 4, 6, 8, 10, 12... and the smallest multiple missing from nums is 10.

from typing import List

class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        # Use x as a bitmask to mark which multiples of k are present.
        # For example, if k = 3:
        # 3  -> bit 0
        # 6  -> bit 1
        # 9  -> bit 2
        x = 0

        for n in nums:
            # Consider only numbers that are multiples of k.
            if not (n % k):

                # Convert the multiple into its corresponding bit index.
                # k -> 0, 2k -> 1, 3k -> 2, ...
                i = (n // k) - 1

                # Mark this multiple as present in the bitmask.
                x |= 1 << i

        # (x + 1) & ~x isolates the lowest unset bit.
        # Its bit position represents the smallest missing multiple of k.
        return ((x + 1) & ~x).bit_length() * k