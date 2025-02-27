# https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/

# Example 1:
# Input: arr = [1,2,3,4,5,6,7,8]
# Output: 5
# Explanation: The longest subsequence that is fibonacci-like: [1,2,3,5,8].

from typing import List
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[0] * n for _ in range(n)]  # DP table to store sequence lengths
        longest_seq = 0  # Tracks the longest Fibonacci-like subsequence

        for curr_idx in range(2, n):
            left, right = 0, curr_idx - 1  # Two pointers for checking pairs
            while left < right:
                pair_sum = arr[left] + arr[right]
                if pair_sum > arr[curr_idx]:  # Decrease right pointer if sum is too large
                    right -= 1
                elif pair_sum < arr[curr_idx]:  # Increase left pointer if sum is too small
                    left += 1
                else:
                    dp[right][curr_idx] = dp[left][right] + 1  # Update DP table
                    longest_seq = max(dp[right][curr_idx], longest_seq)  # Update max length
                    right -= 1
                    left += 1

        return longest_seq + 2 if longest_seq else 0  # Include the first two elements in the count
