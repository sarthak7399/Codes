# https://leetcode.com/problems/maximize-subarrays-after-removing-one-conflicting-pair/

# Example 1:
# Input: n = 4, conflictingPairs = [[2,3],[1,4]]
# Output: 9
# Explanation:
# Remove [2, 3] from conflictingPairs. Now, conflictingPairs = [[1, 4]].
# There are 9 subarrays in nums where [1, 4] do not appear together. They are [1], [2], [3], [4], [1, 2], [2, 3], [3, 4], [1, 2, 3] and [2, 3, 4].
# The maximum number of subarrays we can achieve after removing one element from conflictingPairs is 9.

from typing import List

class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        
        # Group all `u` values by their `v` endpoint
        right = [[] for _ in range(n + 1)]
        for a, b in conflictingPairs:
            right[max(a, b)].append(min(a, b))
        
        # Base score
        ans = 0 
        # `left` stores [top1, top2] `u` values seen so far, where top1 >= top2.
        # `left[0]` acts as our running `forbidden_start`.
        left = [0, 0] 
        # `bonus[u]` accumulates the total gain if the critical conflict involving `u` is removed.
        bonus = [0] * (n + 1)
        
        # Single pass from r = 1 to n
        for r in range(1, n + 1):
            # Check for new conflicts ending at `r` and update `left`
            for l in right[r]:
                # This is a concise trick to update the top two seen values
                if l > left[0]:
                    left = [l, left[0]]
                elif l > left[1]:
                    left = [left[0], l]
            
            # Add the count for this endpoint to the base score
            ans += r - left[0]

            # The gain at this step is the difference between the top two forbidden starts.
            # We add this gain to the tally for the `u` value causing the restriction (`left[0]`).
            if left[0] > 0:
                bonus[left[0]] += left[0] - left[1]
        
        # The final result is the base score plus the maximum possible gain.
        return ans + max(bonus)