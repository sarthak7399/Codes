# https://leetcode.com/problems/find-lucky-integer-in-an-array/

# Example 1:
# Input: arr = [2,2,3,4]
# Output: 2
# Explanation: The only lucky number in the array is 2 because frequency[2] == 2.

from typing import List

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        from collections import Counter
        
        # Count the frequency of each number in the array
        freq = Counter(arr)

        max_lucky = -1  # Initialize to -1 (in case no lucky number is found)

        # Iterate through each unique number and its frequency
        for num, count in freq.items():
            # A "lucky" number is one whose value equals its frequency
            if num == count:
                # Track the maximum lucky number encountered so far
                max_lucky = max(max_lucky, num)

        # Return the largest lucky number found, or -1 if none found
        return max_lucky
