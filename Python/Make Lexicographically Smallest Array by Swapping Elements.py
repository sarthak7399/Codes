# https://leetcode.com/problems/make-lexicographically-smallest-array-by-swapping-elements/

# Example 1:
# Input: nums = [1,5,3,9,8], limit = 2
# Output: [1,3,5,8,9]
# Explanation: Apply the operation 2 times:
# - Swap nums[1] with nums[2]. The array becomes [1,3,5,9,8]
# - Swap nums[3] with nums[4]. The array becomes [1,3,5,8,9]
# We cannot obtain a lexicographically smaller array by applying any more operations.
# Note that it may be possible to get the same result by doing different operations.

from typing import List
class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        # Pair each number with its index and sort by the number
        sorted_enum = sorted((num, i) for i, num in enumerate(nums))
        
        new_positions = []
        curr_positions = []
        prev = float('-inf')
        
        for num, idx in sorted_enum:
            # If the current number exceeds the previous number by more than the limit,
            # sort and append the current positions to the result
            if num > prev + limit:
                new_positions.extend(sorted(curr_positions))
                curr_positions = [idx]
            else:
                curr_positions.append(idx)
            prev = num
        
        # Append any remaining positions
        new_positions.extend(sorted(curr_positions))
        
        # Construct the result array using the new positions
        res = [0] * n
        for i, idx in enumerate(new_positions):
            res[idx] = sorted_enum[i][0]
        
        return res