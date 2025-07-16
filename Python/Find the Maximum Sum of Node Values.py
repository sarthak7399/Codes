# https://leetcode.com/problems/find-the-maximum-sum-of-node-values/

# Example 1:
# Input: nums = [1,2,1], k = 3, edges = [[0,1],[0,2]]
# Output: 6
# Explanation: Alice can achieve the maximum sum of 6 using a single operation:
# - Choose the edge [0,2]. nums[0] and nums[2] become: 1 XOR 3 = 2, and the array nums becomes: [1,2,1] -> [2,2,2].
# The total sum of values is 2 + 2 + 2 = 6.
# It can be shown that 6 is the maximum achievable sum of values.

from typing import List

class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
#---------------------------------------------------------------------
        # Solution 2: O(1) extra space 
#---------------------------------------------------------------------
        base = sum(nums)     # Base sum of original values
        sum_pos = cnt_pos = 0
        min_pos = float('inf')
        best_nonpos = float('-inf')
        for x in nums:
            d = (x ^ k) - x  # Compute delta on the fly
            if d > 0:        # Positive improvement
                cnt_pos += 1
                sum_pos += d
                min_pos = min(min_pos, d)
            else:            # Non-positive (zero or negative)
                best_nonpos = max(best_nonpos, d)

        if cnt_pos % 2 == 0: # if even count of positives,
            return base + sum_pos # we can take them all

        loss = min(min_pos, -best_nonpos) # sacrifice the smaller loss
        return base + sum_pos - loss

#---------------------------------------------------------------------
        # Solution 1: O(n) extra space, first approach 
#---------------------------------------------------------------------
        base = sum(nums) # Base sum & compute deltas
        deltas = [(x ^ k) - x for x in nums]
        sum_pos = cnt_pos = 0
        min_pos = float('inf')
        best_nonpos = float('-inf')
        for d in deltas: # Collect pos deltas & track smallest pos
            if d > 0:
                cnt_pos += 1
                sum_pos += d
                min_pos = min(min_pos, d)
            else:
                best_nonpos = max(best_nonpos, d)

        if cnt_pos % 2 == 0:      # If count of positives even, 
            return base + sum_pos # then we take them all
        loss = min(min_pos, -best_nonpos) # Else, sacrifice the smaller loss
        return base + sum_pos - loss