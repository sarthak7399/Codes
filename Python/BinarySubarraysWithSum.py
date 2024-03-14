# https://leetcode.com/problems/binary-subarrays-with-sum/description/?envType=daily-question&envId=2024-03-14

# Example 1:
# Input: nums = [1,0,1,0,1], goal = 2
# Output: 4
# Explanation: The 4 subarrays are bolded and underlined below:
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]

from typing import List
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = {0: 1}  # Initialize a dictionary to store counts of cumulative sums
        curr_sum = 0  # Initialize the current sum
        total_subarrays = 0  # Initialize the total count of subarrays with the given sum
        
        for num in nums:  # Iterate through the numbers in the array
            curr_sum += num  # Update the current sum
            if curr_sum - goal in count:  # Check if there is a subarray with sum equal to 'goal'
                total_subarrays += count[curr_sum - goal]  # Update the total count of subarrays
            count[curr_sum] = count.get(curr_sum, 0) + 1  # Update the count of cumulative sums
        
        return total_subarrays  # Return the total count of subarrays with the given sum
