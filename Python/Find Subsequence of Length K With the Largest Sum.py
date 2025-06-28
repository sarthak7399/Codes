# https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/

# Example 1:
# Input: nums = [2,1,3,3], k = 2
# Output: [3,3]
# Explanation:
# The subsequence has the largest sum of 3 + 3 = 6.

from typing import List

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Pair each element with its index using enumerate
        # enumerate(nums) returns (index, value) pairs, but we reverse them to (value, index)
        # This allows us to sort by value while keeping track of original indices
        indexed = [(val, idx) for idx, val in enumerate(nums)]

        # Step 2: Sort the pairs in descending order by value
        # lambda x: -x[0] means we sort by the first element of the pair (the value), in descending order
        indexed.sort(key=lambda x: -x[0])

        # Step 3: Take the top k elements with the highest values
        # These are the most significant values, regardless of their original order
        top_k = indexed[:k]

        # Step 4: Sort the top k elements by their original indices to restore their order in the array
        # lambda x: x[1] sorts by the second element of the pair (the original index)
        top_k.sort(key=lambda x: x[1])

        # Step 5: Extract just the values (ignoring indices) to return the final subsequence
        return [val for val, _ in top_k]
