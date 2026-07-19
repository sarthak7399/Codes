# https://leetcode.com/problems/count-special-triplets/

# Example 1:
# Input: nums = [6,3,6]
# Output: 1
# Explanation:
# The only special triplet is (i, j, k) = (0, 1, 2), where:
# nums[0] = 6, nums[1] = 3, nums[2] = 6
# nums[0] = nums[1] * 2 = 3 * 2 = 6
# nums[2] = nums[1] * 2 = 3 * 2 = 6

class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        max_val = max(nums) * 2

        # Frequency of values seen so far (left side)
        freqPrev = [0] * (max_val + 1)
        # Frequency of values ahead (right side)
        freqNext = [0] * (max_val + 1)

        # Build initial right-side frequency
        for x in nums:
            freqNext[x] += 1

        ans = 0
        for x in nums:
            freqNext[x] -= 1        # Move x from right to current
            t = x * 2               # Target value for triplet
            ans = (ans + freqPrev[t] * freqNext[t]) % MOD
            freqPrev[x] += 1        # Add x to left side

        return ans
