# https://leetcode.com/problems/24-game/

# Example 1:
# Input: cards = [4,1,8,7]
# Output: true
# Explanation: (8-4) * (7-1) = 24

from typing import List

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        # Small tolerance to handle floating-point precision errors
        EPS = 1e-6

        # Depth-First Search (DFS) helper function
        def dfs(nums: List[float]) -> bool:
            # Base case: if only one number remains, check if it's (almost) 24
            if len(nums) == 1:
                return abs(nums[0] - 24.0) < EPS

            # Try every pair of numbers (order matters for -, /)
            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i == j:  # Skip using the same number twice
                        continue

                    # Build new list excluding nums[i] and nums[j]
                    next_nums = [nums[k] for k in range(len(nums)) if k != i and k != j]

                    a, b = nums[i], nums[j]

                    # Generate all possible results of combining a and b
                    candidates = [a + b, a - b, b - a, a * b]

                    # Division (check for division by zero using EPS)
                    if abs(b) > EPS:
                        candidates.append(a / b)
                    if abs(a) > EPS:
                        candidates.append(b / a)

                    # Recursively check each candidate by adding it back to the list
                    for val in candidates:
                        if dfs(next_nums + [val]):
                            return True
            return False

        # Convert integers to floats and start DFS
        return dfs([float(x) for x in cards])
