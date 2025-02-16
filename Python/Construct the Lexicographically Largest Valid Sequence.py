# https://leetcode.com/problems/construct-the-lexicographically-largest-valid-sequence/

# Example 1:
# Input: n = 3
# Output: [3,1,2,3,2]
# Explanation: [2,3,2,1,3] is also a valid sequence, but [3,1,2,3,2] is the lexicographically largest valid sequence.

from typing import List
class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        res = [0] * (2 * n - 1)  # Initialize result array with 0s
        seen = set()  # Track used numbers

        def backtrack(i):
            if i == len(res):  # If all positions are filled, return True
                return True
            if res[i]:  # Skip already filled positions
                return backtrack(i + 1)

            for j in range(n, 0, -1):  # Try placing numbers from n to 1
                if j in seen:
                    continue

                seen.add(j)
                res[i] = j

                if j == 1:  # Special case for 1 (appears once)
                    if backtrack(i + 1):
                        return True
                elif i + j < len(res) and res[i + j] == 0:  # Ensure valid placement
                    res[i + j] = j
                    if backtrack(i + 1):
                        return True
                    res[i + j] = 0  # Backtrack if needed

                res[i] = 0  # Reset position
                seen.remove(j)  # Remove number from used set

            return False  # No valid sequence found

        backtrack(0)
        return res
