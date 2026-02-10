# https://leetcode.com/problems/longest-balanced-subarray-i/

# Example 1:
# Input: nums = [2,5,4,3]
# Output: 4
# Explanation:
# The longest balanced subarray is [2, 5, 4, 3].
# It has 2 distinct even numbers [2, 4] and 2 distinct odd numbers [5, 3]. Thus, the answer is 4.

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        seen = set()          # tracks unique numbers in current subarray
        Len = 0               # length of the longest balanced subarray found

        for l in range(n):
            # If remaining elements cannot beat current best length, stop early
            if l > n - Len:
                break

            diff = 0          # balance: +1 for even, -1 for odd (unique only)

            for r in range(l, n):
                x = nums[r]

                # Process only if number appears first time in this subarray
                if x not in seen:
                    # even → +1, odd → -1
                    diff += 1 - (x & 1) * 2
                    seen.add(x)

                # If balance is zero, subarray [l..r] is balanced
                if diff == 0:
                    Len = max(Len, r - l + 1)

            # Clear set before moving left pointer
            seen.clear()

        return Len
