

# Example 1:
# Input: nums = [1,2,3,1,2,3,1,2], k = 2
# Output: 6
# Explanation: The longest possible good subarray is [1,2,3,1,2,3] since the values 1, 2, and 3 occur at most twice in this subarray. Note that the subarrays [2,3,1,2,3,1] and [3,1,2,3,1,2] are also good.
# It can be shown that there are no good subarrays with length more than 6.

from typing import List
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        ans = 0                    # Initialize the maximum length of the "good" subarray
        mp = {}                    # Initialize a dictionary to store the frequency of elements
        l = 0                      # Initialize the left pointer
        n = len(nums)              # Get the length of the nums array
        for r in range(n):         # Iterate through the nums array with the right pointer
            mp[nums[r]] = mp.get(nums[r], 0) + 1  # Update the frequency of nums[r] in the dictionary
            if mp[nums[r]] > k:    # If the frequency of nums[r] exceeds k
                while nums[l] != nums[r]:  # Move the left pointer until nums[l] becomes equal to nums[r]
                    mp[nums[l]] -= 1       # Decrease the frequency of nums[l] in the dictionary
                    l += 1                 # Move the left pointer to the right
                mp[nums[l]] -= 1            # Decrease the frequency of nums[l] in the dictionary
                l += 1                       # Move the left pointer to the right
            ans = max(ans, r - l + 1)        # Update the maximum length of the "good" subarray
        return ans                            # Return the maximum length of the "good" subarray
