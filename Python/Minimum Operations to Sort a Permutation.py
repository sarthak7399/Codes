# https://leetcode.com/problems/minimum-operations-to-sort-a-permutation/

# Example 1:
# Input: nums = [0,2,1]
# Output: 2
# Explanation:
# Rotate Left by one: [2, 1, 0]
# Reverse the array: [0, 1, 2]
# The array becomes sorted in 2 operations, which is minimal

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # Length of the array.
        n = len(nums)

        # Target arrangement: [0, 1, 2, ..., n - 1].
        want = list(range(n))

        # Find the index of 0, which determines the rotation point.
        i = nums.index(0)

        # Check if rotating the array left from index i produces
        # the target arrangement.
        if nums[i:] + nums[:i] == want:
            # Return the minimum operations based on the rotation position.
            return min(i, n - i + 2)

        # Check if reversing the two parts around index i produces
        # the target arrangement.
        if nums[i::-1] + nums[:i:-1] == want:
            # Return the minimum operations for this arrangement.
            return min(i + 2, n - i)

        # Neither arrangement matches the target.
        return -1