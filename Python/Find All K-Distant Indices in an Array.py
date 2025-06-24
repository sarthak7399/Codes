# https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/

# Example 1:
# Input: nums = [3,4,9,1,3,9,5], key = 9, k = 1
# Output: [1,2,3,4,5,6]
# Explanation: Here, nums[2] == key and nums[5] == key.
# - For index 0, |0 - 2| > k and |0 - 5| > k, so there is no j where |0 - j| <= k and nums[j] == key. Thus, 0 is not a k-distant index.
# - For index 1, |1 - 2| <= k and nums[2] == key, so 1 is a k-distant index.
# - For index 2, |2 - 2| <= k and nums[2] == key, so 2 is a k-distant index.
# - For index 3, |3 - 2| <= k and nums[2] == key, so 3 is a k-distant index.
# - For index 4, |4 - 5| <= k and nums[5] == key, so 4 is a k-distant index.
# - For index 5, |5 - 5| <= k and nums[5] == key, so 5 is a k-distant index.
# - For index 6, |6 - 5| <= k and nums[5] == key, so 6 is a k-distant index.
# Thus, we return [1,2,3,4,5,6] which is sorted in increasing order. 

from typing import List

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        ans = []
        j = 0  # Pointer to avoid revisiting indices

        for i, x in enumerate(nums):
            if x == key:
                # Define the window of indices within distance k from index i
                up = min(n - 1, i + k)      # Upper limit for j
                j = max(j, i - k)           # Start j from the maximum of current j or i-k
                while j <= up:
                    ans.append(j)          # Add all indices within distance k of key
                    j += 1                 # Move to the next index

        return ans
