# https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/

# Example 1:
# Input: nums = [2,11,10,1,3], k = 10
# Output: 2
# Explanation:
# In the first operation, we remove elements 1 and 2, then add 1 * 2 + 2 to nums. nums becomes equal to [4, 11, 10, 3].
# In the second operation, we remove elements 3 and 4, then add 3 * 2 + 4 to nums. nums becomes equal to [10, 11, 10].
# At this stage, all the elements of nums are greater than or equal to 10 so we can stop. 
# It can be shown that 2 is the minimum number of operations needed so that all elements of the array are greater than or equal to 10.

import heapq
class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Convert nums into a min-heap to always access the smallest elements first
        heapq.heapify(nums)
        operations = 0  # Count the number of operations performed

        # Process elements while the heap is not empty
        for _ in range(len(nums)):
            smallest = heapq.heappop(nums)  # Extract the smallest element
            
            # If the smallest element is already >= k, no more operations needed
            if smallest >= k:
                break
            
            operations += 1  # Increase operation count
            second_smallest = heapq.heappop(nums)  # Get the second smallest element
            
            # Compute the new element and push it back into the heap
            new_value = smallest * 2 + second_smallest if smallest < second_smallest else second_smallest * 2 + smallest
            heapq.heappush(nums, new_value)

        return operations  # Return the total operations performed
