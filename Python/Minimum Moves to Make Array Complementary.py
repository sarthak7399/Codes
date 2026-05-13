# https://leetcode.com/problems/minimum-moves-to-make-array-complementary/

# Example 1:
# Input: nums = [1,2,4,3], limit = 4
# Output: 1
# Explanation: In 1 move, you can change nums to [1,2,2,3] (underlined elements are changed).
# nums[0] + nums[3] = 1 + 3 = 4.
# nums[1] + nums[2] = 2 + 2 = 4.
# nums[2] + nums[1] = 2 + 2 = 4.
# nums[3] + nums[0] = 3 + 1 = 4.
# Therefore, nums[i] + nums[n-1-i] = 4 for every i, so nums is complementary.

from typing import List

class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        
        n = len(nums)

        # Difference array to track move changes for each possible target sum
        diff = [0] * (2 * limit + 2)

        # Process symmetric pairs
        for i in range(n // 2):

            # Smaller and larger value in the pair
            a = min(nums[i], nums[n - 1 - i])
            b = max(nums[i], nums[n - 1 - i])

            # Initially, every pair requires 2 moves
            #
            # For sums in range [a+1, b+limit],
            # only 1 move is needed
            diff[a + 1] -= 1
            diff[b + limit + 1] += 1

            # For exact sum (a+b),
            # 0 moves are needed
            diff[a + b] -= 1
            diff[a + b + 1] += 1

        pairs = n // 2

        # Start assuming every pair needs 2 moves
        current = pairs * 2

        answer = float('inf')

        # Try every possible target sum
        for target_sum in range(2, 2 * limit + 1):

            # Apply difference array updates
            current += diff[target_sum]

            # Track minimum moves required
            answer = min(answer, current)

        return answer