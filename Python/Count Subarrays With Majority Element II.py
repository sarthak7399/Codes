# https://leetcode.com/problems/count-subarrays-with-majority-element-ii/

# Example 1:
# Input: nums = [1,2,2,3], target = 2
# Output: 5
# Explanation:
# Valid subarrays with target = 2 as the majority element:
# nums[1..1] = [2]
# nums[2..2] = [2]
# nums[1..2] = [2,2]
# nums[0..2] = [1,2,2]
# nums[1..3] = [2,2,3]
# So there are 5 such subarrays.

from typing import List

class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        # Prefix balance.
        # We start from n to avoid negative indices when using the
        # frequency array.
        pref = n

        # freq[i] = number of times a particular prefix balance
        # has appeared so far.
        freq = [0] * (2 * n + 1)

        # Initial prefix balance (before processing any element)
        freq[n] = 1

        # Number of valid prefixes that can form a subarray
        # where target is the majority element.
        less = 0

        # Final answer
        ans = 0

        for num in nums:

            # Treat:
            # target      -> +1
            # non-target  -> -1
            #
            # A subarray has target as majority if its balance > 0.

            if num == target:
                # Adding +1 increases the balance.
                # Prefixes with the current balance now become valid.
                less += freq[pref]

                pref += 1
            else:
                # Adding -1 decreases the balance.
                pref -= 1

                # Prefixes with this new balance are no longer valid.
                less -= freq[pref]

            # Record the current prefix balance
            freq[pref] += 1

            # Add the number of valid subarrays ending here
            ans += less

        return ans