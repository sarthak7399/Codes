# https://leetcode.com/problems/stone-game-v/

# Example 1:
# Input: stoneValue = [6,2,3,4,5,5]
# Output: 18
# Explanation: In the first round, Alice divides the row to [6,2,3], [4,5,5]. The left row has the value 11 and the right row has value 14. Bob throws away the right row and Alice's score is now 11.
# In the second round Alice divides the row to [6], [2,3]. This time Bob throws away the left row and Alice's score becomes 16 (11 + 5).
# The last round Alice has only one choice to divide the row which is [2], [3]. Bob throws away the right row and Alice's score is now 18 (16 + 2). The game ends because only one stone is remaining in the row.

from typing import List

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        # Number of stones
        n = len(stoneValue)

        # prefix[i] stores the sum of elements from index 0 to i - 1.
        # This allows us to calculate any subarray sum in O(1).
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        # dp[l][r] = maximum score obtainable from subarray [l, r].
        dp = [[0] * n for _ in range(n)]

        # left_best[l][r] stores the best value of:
        # dp[l][k] + sum(l, k) for splits where the left part is chosen.
        left_best = [[0] * n for _ in range(n)]

        # right_best[l][r] stores the best value of:
        # dp[k][r] + sum(k, r) for splits where the right part is chosen.
        right_best = [[0] * n for _ in range(n)]

        # Pointers used to efficiently find valid split positions.
        left_ptr = [0] * n
        right_ptr = list(range(n))

        # Initialise the single-element subarrays.
        for i in range(n):
            left_best[i][i] = stoneValue[i]
            right_best[i][i] = stoneValue[i]

            # Initially, there is no valid split to the left.
            left_ptr[i] = i - 1

            # Start the right pointer at the beginning of the range.
            right_ptr[i] = i

        # Process subarrays in increasing order of length.
        for length in range(2, n + 1):
            for l in range(n - length + 1):
                r = l + length - 1

                # Calculate the total sum of the current subarray.
                total = prefix[r + 1] - prefix[l]

                # Move left_ptr to find the largest split k where
                # 2 * left_sum <= total.
                while left_ptr[l] + 1 <= r - 1:
                    k = left_ptr[l] + 1
                    left_sum = prefix[k + 1] - prefix[l]

                    # Stop when the left part becomes larger than
                    # half of the total sum.
                    if 2 * left_sum > total:
                        break

                    left_ptr[l] += 1

                # Move right_ptr to find the first split k where
                # 2 * left_sum >= total.
                while right_ptr[l] <= r - 1:
                    k = right_ptr[l]
                    left_sum = prefix[k + 1] - prefix[l]

                    # Stop once the left part reaches at least half
                    # of the total sum.
                    if 2 * left_sum >= total:
                        break

                    right_ptr[l] += 1

                # Store the best score for the current subarray.
                best = 0

                # If the left part is smaller or equal to the right part,
                # we can keep the left part and add its accumulated score.
                if left_ptr[l] >= l:
                    best = left_best[l][left_ptr[l]]

                # If the right part is smaller or equal to the left part,
                # we can keep the right part.
                if right_ptr[l] <= r - 1:
                    best = max(
                        best,
                        right_best[right_ptr[l] + 1][r]
                    )

                dp[l][r] = best

                # Update the best value for future splits involving
                # the current left boundary.
                left_best[l][r] = max(
                    left_best[l][r - 1],
                    dp[l][r] + total
                )

                # Update the best value for future splits involving
                # the current right boundary.
                right_best[l][r] = max(
                    right_best[l + 1][r],
                    dp[l][r] + total
                )

        # Return the maximum score obtainable from the entire array.
        return dp[0][n - 1]