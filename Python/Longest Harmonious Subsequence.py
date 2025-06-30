# https://leetcode.com/problems/longest-harmonious-subsequence/

# Example 1:
# Input: nums = [1,3,2,2,5,2,3,7]
# Output: 5
# Explanation:
# The longest harmonious subsequence is [3,2,2,2,3].

from collections import Counter
from typing import List

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        # Count the frequency of each number in the array
        freq = Counter(nums)

        max_len = 0  # To store the maximum length of harmonious subsequence

        # Iterate through each unique number in the frequency map
        for num in freq:
            # Check if there exists a number that is exactly 1 greater
            if num + 1 in freq:
                # A harmonious subsequence requires two numbers with a difference of exactly 1
                # So, we add their frequencies to get the length of that subsequence
                max_len = max(max_len, freq[num] + freq[num + 1])

        return max_len
