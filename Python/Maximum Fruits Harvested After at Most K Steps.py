# https://leetcode.com/problems/maximum-fruits-harvested-after-at-most-k-steps/

# Example 1:
# Input: fruits = [[2,8],[6,3],[8,6]], startPos = 5, k = 4
# Output: 9
# Explanation: 
# The optimal way is to:
# - Move right to position 6 and harvest 3 fruits
# - Move right to position 8 and harvest 6 fruits
# You moved 3 steps and harvested 3 + 6 = 9 fruits in total.

class Solution:
    def maxTotalFruits(self, fruits, startPos: int, k: int) -> int:
        left = 0                 # Left pointer of sliding window
        total = 0                # Total number of fruits in current window
        res = 0                  # Result to store maximum fruits collected

        # Iterate with right pointer over each fruit's position and count
        for right in range(len(fruits)):
            total += fruits[right][1]   # Add current fruit's quantity to total

            # Check if the cost (steps needed) to visit current window exceeds k
            # Two possible paths:
            # 1. Go left first to fruits[left][0], then right to fruits[right][0]
            # 2. Go right first to fruits[right][0], then left to fruits[left][0]
            # Choose the minimum of these two costs
            while left <= right and min(
                abs(startPos - fruits[left][0]) + fruits[right][0] - fruits[left][0],
                abs(startPos - fruits[right][0]) + fruits[right][0] - fruits[left][0]
            ) > k:
                # If cost exceeds k, shrink window from left
                total -= fruits[left][1]   # Remove fruits at left from total
                left += 1

            # Update result if current window total is higher
            res = max(res, total)

        # Return maximum fruits that can be collected within k steps
        return res
