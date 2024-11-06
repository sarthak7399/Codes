# https://leetcode.com/problems/find-if-array-can-be-sorted/

# Example 1:
# Input: nums = [8,4,2,30,15]
# Output: true
# Explanation: Let's look at the binary representation of every element. The numbers 2, 4, and 8 have one set bit each with binary representation "10", "100", and "1000" respectively. The numbers 15 and 30 have four set bits each with binary representation "1111" and "11110".
# We can sort the array using 4 operations:
# - Swap nums[0] with nums[1]. This operation is valid because 8 and 4 have one set bit each. The array becomes [4,8,2,30,15].
# - Swap nums[1] with nums[2]. This operation is valid because 8 and 2 have one set bit each. The array becomes [4,2,8,30,15].
# - Swap nums[0] with nums[1]. This operation is valid because 4 and 2 have one set bit each. The array becomes [2,4,8,30,15].
# - Swap nums[3] with nums[4]. This operation is valid because 30 and 15 have four set bits each. The array becomes [2,4,8,15,30].
# The array has become sorted, hence we return true.
# Note that there may be other sequences of operations which also sort the array.

from typing import List

class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        # Initialize previous maximum, current minimum, and current maximum in a group
        prev_group_max = float('-inf')
        curr_group_min = curr_group_max = curr_bit_count = 0
        
        # Loop through each number in the array
        for num in nums:
            # Count set bits in the current number's binary representation
            num_bit_count = num.bit_count()
            
            # Check if the current number has the same set bit count as the previous
            if curr_bit_count == num_bit_count:
                # Update the current minimum and maximum for this group
                curr_group_min = min(curr_group_min, num)
                curr_group_max = max(curr_group_max, num)
            
            # If the set bit count has changed, check the group ordering
            elif curr_group_min < prev_group_max:
                return False
            
            else:
                # Update the previous group max to the current max and reset group bounds
                prev_group_max = curr_group_max
                curr_group_min = curr_group_max = num
                curr_bit_count = num_bit_count
        
        # Final check to ensure that the last group's min is not less than previous max
        return curr_group_min >= prev_group_max
