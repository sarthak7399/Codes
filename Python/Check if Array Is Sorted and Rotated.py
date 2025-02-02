# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/

# Example 1:
# Input: nums = [3,4,5,1,2]
# Output: true
# Explanation: [1,2,3,4,5] is the original sorted array.
# You can rotate the array by x = 3 positions to begin on the the element of value 3: [3,4,5,1,2].

class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)  # Get the length of the list
        cnt = 0  # Initialize count of decreases

        for i in range(1, n):  # Iterate through the list
            if nums[i-1] > nums[i]:  # Check if previous element is greater
                cnt += 1  # Increment count if a decrease is found

        if nums[0] < nums[n-1]:  # Check if the list can be rotated
            cnt += 1  # Increment count if the first element is smaller than the last

        return cnt <= 1  # Return True if there is at most one decrease
