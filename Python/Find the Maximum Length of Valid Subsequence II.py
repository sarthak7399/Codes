# https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-ii/

# Example 1:
# Input: nums = [1,2,3,4,5], k = 2
# Output: 5
# Explanation:
# The longest valid subsequence is [1, 2, 3, 4, 5].

class Solution:
    def maximumLength(self, nums: list[int], k: int) -> int:
        max_length = 2  # Initialize the maximum subsequence length found so far (at least 2)

        # Try to build subsequences whose total sum modulo k equals target_mod
        for target_mod in range(k):
            remainder_dp = [0] * k  # remainder_dp[r]: longest subsequence ending with remainder r

            for num in nums:
                num_mod = num % k  # Compute remainder of current number modulo k

                # Find what remainder should be before this number so that total modulo equals target_mod
                required_mod = (target_mod - num_mod + k) % k

                # Update: extend the subsequence by adding current number
                remainder_dp[num_mod] = remainder_dp[required_mod] + 1

            # Update overall maximum length
            max_length = max(max_length, max(remainder_dp))

        return max_length
