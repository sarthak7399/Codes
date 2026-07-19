# https://leetcode.com/problems/new-21-game/

# Example 2:
# Input: n = 6, k = 1, maxPts = 10
# Output: 0.60000
# Explanation: Alice gets a single card, then stops.
# In 6 out of 10 possibilities, she is at or below 6 points.

class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        # Special case:
        # If k == 0, Alice stops immediately → score = 0 ≤ n → prob = 1
        # If n >= k + maxPts - 1, Alice can never exceed n (max possible score ≤ n)
        # So probability is 1
        if k == 0 or n >= k + maxPts - 1:
            return 1.0

        # dp[i] = probability of reaching exactly i points
        dp = [0.0] * (n + 1)
        dp[0] = 1  # Starting point: probability of score 0 is 1

        # Sliding window sum of last 'maxPts' dp values
        wsum = 1.0  

        # Final answer accumulator (probability of ending with score ≤ n)
        prob = 0.0  

        # Left boundary of the sliding window
        l = 0  

        # Iterate through possible scores 1 to n
        for r in range(1, n + 1):
            # Probability of reaching score r = average of last maxPts states
            dp[r] = wsum / maxPts

            if r < k:
                # If score < k, Alice continues drawing → include dp[r] in window
                wsum += dp[r]
            else:
                # If score ≥ k, Alice stops drawing → add to final probability
                prob += dp[r]

            # Maintain sliding window size (remove old values)
            if r >= maxPts:
                wsum -= dp[l]
                l += 1

        return prob
