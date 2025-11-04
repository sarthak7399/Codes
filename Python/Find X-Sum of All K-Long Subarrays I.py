# https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-i/

# Example 1:
# Input: nums = [1,1,2,2,3,4,2,3], k = 6, x = 2
# Output: [6,10,12]
# Explanation:
# For subarray [1, 1, 2, 2, 3, 4], only elements 1 and 2 will be kept in the resulting array. Hence, answer[0] = 1 + 1 + 2 + 2.
# For subarray [1, 2, 2, 3, 4, 2], only elements 2 and 4 will be kept in the resulting array. Hence, answer[1] = 2 + 2 + 2 + 4. Note that 4 is kept in the array since it is bigger than 3 and 1 which occur the same number of times.
# For subarray [2, 2, 3, 4, 2, 3], only elements 2 and 3 are kept in the resulting array. Hence, answer[2] = 2 + 2 + 2 + 3 + 3.

from collections import defaultdict
from typing import List

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        """
        For each sliding window of size k in the array 'nums',
        compute the sum of the top 'x' most frequent elements,
        where each element contributes (value * frequency) to the sum.
        """

        n = len(nums)
        freq = defaultdict(int)  # Stores frequency of elements in the current window

        # Step 1: Initialize frequency map for the first window
        for i in range(k):
            freq[nums[i]] += 1

        # Helper function to compute the 'X-sum' for a given frequency map
        def compute_x_sum(freq, x):
            # Convert frequency dictionary to a list of (value, frequency) pairs
            items = [(v, f) for v, f in freq.items()]

            # Sort primarily by frequency (descending), then by value (descending)
            items.sort(key=lambda t: (-t[1], -t[0]))

            # Compute total for top 'x' items
            total = 0
            for i in range(min(x, len(items))):
                v, f = items[i]
                total += v * f
            return total

        # Step 2: Compute X-sum for the first window
        ans = [compute_x_sum(freq, x)]

        # Step 3: Slide the window one element at a time
        for i in range(k, n):
            add = nums[i]        # New element entering the window
            rem = nums[i - k]    # Old element leaving the window

            # Update frequencies
            freq[add] += 1
            freq[rem] -= 1

            # Remove element completely if its frequency becomes 0
            if freq[rem] == 0:
                del freq[rem]

            # Compute X-sum for the updated window
            ans.append(compute_x_sum(freq, x))

        # Step 4: Return list of all X-sums for each window
        return ans
