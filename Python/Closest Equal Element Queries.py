# https://leetcode.com/problems/closest-equal-element-queries/

# Example 1:
# Input: nums = [1,3,1,4,1,3,2], queries = [0,3,5]
# Output: [2,-1,3]
# Explanation:
# Query 0: The element at queries[0] = 0 is nums[0] = 1. The nearest index with the same value is 2, and the distance between them is 2.
# Query 1: The element at queries[1] = 3 is nums[3] = 4. No other index contains 4, so the result is -1.
# Query 2: The element at queries[2] = 5 is nums[5] = 3. The nearest index with the same value is 1, and the distance between them is 3 (following the circular path: 5 -> 6 -> 0 -> 1).

from typing import List

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)  # Length of the array

        positions = {}  # Map each number to list of its indices

        # Build the positions dictionary
        for i, num in enumerate(nums):
            if num not in positions:
                positions[num] = []
            positions[num].append(i)

        # Initialize answer array with -1 (default if no valid pair exists)
        answer = [-1] * n

        # Process each group of indices (same numbers)
        for pos in positions.values():
            m = len(pos)

            # If only one occurrence, no valid circular distance
            if m == 1:
                continue

            # For each index in this group
            for i in range(m):
                curr = pos[i]  # Current index

                # Previous occurrence in circular manner
                prev_idx = pos[(i - 1 + m) % m]

                # Next occurrence in circular manner
                next_idx = pos[(i + 1) % m]

                # Distance to previous (circular)
                dist_prev = abs(curr - prev_idx)
                dist_prev = min(dist_prev, n - dist_prev)

                # Distance to next (circular)
                dist_next = abs(curr - next_idx)
                dist_next = min(dist_next, n - dist_next)

                # Store minimum of both distances
                answer[curr] = min(dist_prev, dist_next)

        # Return results for the queried indices
        return [answer[idx] for idx in queries]