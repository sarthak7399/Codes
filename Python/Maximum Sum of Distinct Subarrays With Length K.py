# https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/

# Example 1:
# Input: nums = [1,5,4,2,9,9,9], k = 3
# Output: 15
# Explanation: The subarrays of nums with length 3 are:
# - [1,5,4] which meets the requirements and has a sum of 10.
# - [5,4,2] which meets the requirements and has a sum of 11.
# - [4,2,9] which meets the requirements and has a sum of 15.
# - [2,9,9] which does not meet the requirements because the element 9 is repeated.
# - [9,9,9] which does not meet the requirements because the element 9 is repeated.
# We return 15 because it is the maximum subarray sum of all the subarrays that meet the conditions

from typing import List

# Method 1 : Brute Force - Time Complexity O(N^2), Space Complexity O(1)
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        # Set to track unique elements in the current subarray
        hashes = set()
        
        # Initialize pointers, variables for the array size, counter, current sum, and result
        i, j, n, counter, currSum, result = 0, 0, len(nums), 0, 0, -999

        # Iterate while the window defined by `i` and `j` is within bounds
        while (i <= j and j < n):
            counter += 1  # Increment the window size counter

            # Case 1: Expand the window if the current element is unique and within the allowed size (k)
            if ((nums[j] not in hashes) and (counter <= k)):
                hashes.add(nums[j])  # Add the current element to the set
                currSum += nums[j]  # Update the current sum
                j += 1  # Move the right pointer forward

            # If the window size equals `k`, update the result with the maximum sum so far
            if (counter == k): 
                result = max(result, currSum)

            # Case 2: If the window size exceeds `k`, shrink it from the left
            if (j < n and counter > k):
                currSum -= nums[i]  # Subtract the element at the left pointer from the current sum
                hashes.discard(nums[i])  # Remove it from the set
                i += 1  # Move the left pointer forward
                currSum += nums[j]  # Add the new right element to the sum
                hashes.add(nums[j])  # Add the new right element to the set
                j += 1  # Move the right pointer forward
                result = max(result, currSum)  # Update the result

            # Case 3: Reset the window if a duplicate element is encountered
            if (j < n and nums[j] in hashes):
                i += 1  # Move the left pointer forward
                j = i  # Reset the right pointer to match the left pointer
                counter = 0  # Reset the counter
                hashes.clear()  # Clear the set of unique elements
                currSum = 0  # Reset the current sum

        # If no valid subarray was found, return 0; otherwise, return the result
        return 0 if result == -999 else result
    
# Method 2 : Sliding Window - Time Complexity O(N), Space Complexity O(1)
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:

        mSum = float("-inf")
        window = set()
        cSum = 0
        L = 0
        
        for R in range(len(nums)):
            if nums[R] not in window:
                cSum += nums[R]
                window.add(nums[R])
            else:
                # Move left pointer forward to remove duplicates
                while nums[L] != nums[R]:
                    cSum -= nums[L]
                    window.remove(nums[L])
                    L += 1
                L += 1  # Skip the duplicate element
            
            # If the window size is k, update the max sum and shrink the window
            if len(window) == k:
                mSum = max(mSum, cSum)
                # Remove the left element from the window and adjust the sum
                cSum -= nums[L]
                window.remove(nums[L])
                L += 1
        
        return 0 if mSum == float("-inf") else mSum