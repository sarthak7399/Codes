# https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/

# Example 1:
# Input: nums = [3,6,1,2,5], k = 2
# Output: 2
# Explanation:
# We can partition nums into the two subsequences [3,1,2] and [6,5].
# The difference between the maximum and minimum value in the first subsequence is 3 - 1 = 2.
# The difference between the maximum and minimum value in the second subsequence is 6 - 5 = 1.
# Since two subsequences were created, we return 2. It can be shown that 2 is the minimum number of subsequences needed.

from typing import List

class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        # Edge case: if there's only one element, only one partition is needed
        if len(nums) == 1: 
            return 1

        # Find the maximum number in the array
        xMax = max(nums)

        # Frequency array to count occurrences of each number
        freq = [0] * (xMax + 1)
        for x in nums:
            freq[x] += 1

        partitions = 0  # Count of partitions
        x = 0  # Current number to consider

        # Traverse the frequency array to count the number of partitions
        while x <= xMax:
            # Skip numbers not present in the input array
            while x <= xMax and freq[x] == 0:
                x += 1

            if x > xMax:
                break

            # Start a new partition from current number to x + k
            end = x + k
            partitions += 1
            x = end + 1  # Skip to the number after this partition's range

        return partitions
