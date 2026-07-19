# https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i/

# Example 1:
# Input: nums = [5,2,3,1]
# Output: 2
# Explanation:
# The pair (3,1) has the minimum sum of 4. After replacement, nums = [5,2,4].
# The pair (2,4) has the minimum sum of 6. After replacement, nums = [5,6].
# The array nums became non-decreasing in two operations.

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        so = False   # whether array is sorted (non-decreasing)
        ans = 0      # number of operations

        while not so:
            n = len(nums)
            if n == 1:
                return ans

            so = True
            i = 0

            # Track the pair with minimum sum
            ss = nums[0] + nums[1]

            for x in range(n - 1):
                # Update minimum adjacent sum
                if nums[x] + nums[x + 1] < ss:
                    ss = nums[x] + nums[x + 1]
                    i = x

                # Check if array is already non-decreasing
                if nums[x] > nums[x + 1]:
                    so = False

            # If not sorted, merge the minimum-sum adjacent pair
            if not so:
                nums[i] += nums[i + 1]
                nums.pop(i + 1)
                ans += 1

        return ans
