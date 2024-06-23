# https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

# Example 1:
# Input: nums = [8,2,4,7], limit = 4
# Output: 2 
# Explanation: All subarrays are: 
# [8] with maximum absolute diff |8-8| = 0 <= 4.
# [8,2] with maximum absolute diff |8-2| = 6 > 4. 
# [8,2,4] with maximum absolute diff |8-2| = 6 > 4.
# [8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
# [2] with maximum absolute diff |2-2| = 0 <= 4.
# [2,4] with maximum absolute diff |2-4| = 2 <= 4.
# [2,4,7] with maximum absolute diff |2-7| = 5 > 4.
# [4] with maximum absolute diff |4-4| = 0 <= 4.
# [4,7] with maximum absolute diff |4-7| = 3 <= 4.
# [7] with maximum absolute diff |7-7| = 0 <= 4. 
# Therefore, the size of the longest subarray is 2.

from collections import deque
from typing import List
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        """
        This function finds the longest contiguous subarray where the absolute difference
        between the maximum and minimum elements is less than or equal to a given limit.

        Args:
            nums: A list of integers representing the elements in the array.
            limit: An integer representing the maximum allowed difference between
                   the maximum and minimum elements in a subarray.

        Returns:
            The length of the longest subarray satisfying the given condition.
        """

        # Initialize two deques: maxq (stores elements in descending order) and minq (stores elements in ascending order)
        maxq = deque()
        minq = deque()

        # Get the length of the input array
        n = len(nums)

        # Initialize a variable 'j' to keep track of the starting index of the window
        j = 0

        # Initialize a variable 'ans' to store the length of the longest subarray found so far
        ans = 0

        for i in range(n):
            # Maintain maxq in descending order, remove elements smaller than the current element
            while maxq and nums[i] > maxq[-1]:
                maxq.pop()
            # Append the current element to maxq
            maxq.append(nums[i])

            # Maintain minq in ascending order, remove elements larger than the current element
            while minq and nums[i] < minq[-1]:
                minq.pop()
            # Append the current element to minq
            minq.append(nums[i])

            # Check if the difference between max and min elements exceeds the limit
            if maxq[0] - minq[0] > limit:
                # If the first element in maxq is the current element, remove it
                if nums[j] == maxq[0]:
                    maxq.popleft()
                # If the first element in minq is the current element, remove it
                if nums[j] == minq[0]:
                    minq.popleft()
                # Shrink the window from the left side (increment j)
                j += 1

            # Update the maximum length of the subarray found so far
            ans = max(ans, i - j + 1)  # i - j + 1 represents the current window size

        # Return the length of the longest subarray
        return ans
