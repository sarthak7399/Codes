# https://leetcode.com/problems/sum-of-sortable-integers/

# Example 1:
# Input: nums = [3,1,2]
# Output: 3
# Explanation:​​​​​​​
# For n = 3, possible divisors are 1 and 3.
# For k = 1: each subarray has one element. No rotation can sort the array.
# For k = 3: the single subarray [3, 1, 2] can be rotated once to produce [1, 2, 3], which is sorted.
# Only k = 3 is sortable. Hence, the answer is 3.

from typing import List

class Solution:
    def sortableIntegers(self, nums: List[int]) -> int:
        # Length of the input array.
        n = len(nums)

        def check(k):
            # Maximum value from the previous block.
            prev = 0

            # Divide the array into blocks of size k.
            for i in range(0, n, k):
                block = nums[i:i + k]

                # Count descents within the block, where an element
                # is greater than the next element.
                cnt = sum(
                    block[j] > block[j + 1]
                    for j in range(k - 1)
                )

                # Also check the circular boundary from the last
                # element back to the first element.
                if block[-1] > block[0]:
                    cnt += 1

                # Reject if the block has more than one descent
                # or if blocks are not in non-decreasing order.
                if cnt > 1 or prev > min(block):
                    return False

                # Update the maximum value of the current block.
                prev = max(block)

            # All blocks satisfy the required conditions.
            return True

        # Count valid divisors of n.
        ans = 0

        # Check divisors up to the square root of n.
        for k in range(1, int(n**0.5) + 1):
            if n % k == 0:
                # Check the divisor k as a possible block size.
                if check(k):
                    ans += k

                # The paired divisor is n // k.
                other = n // k

                # Avoid checking the same divisor twice for perfect squares.
                if other != k and check(other):
                    ans += other

        # Return the sum of all valid block sizes.
        return ans