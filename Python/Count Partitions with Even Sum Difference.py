# https://leetcode.com/problems/count-partitions-with-even-sum-difference/

# Example 1:
# Input: nums = [10,10,3,7,6]
# Output: 4
# Explanation:
# The 4 partitions are:
# [10], [10, 3, 7, 6] with a sum difference of 10 - 26 = -16, which is even.
# [10, 10], [3, 7, 6] with a sum difference of 20 - 16 = 4, which is even.
# [10, 10, 3], [7, 6] with a sum difference of 23 - 13 = 10, which is even.
# [10, 10, 3, 7], [6] with a sum difference of 30 - 6 = 24, which is even.

class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        # If total sum is odd, it's impossible to split into two equal parts
        if sum(nums) % 2:
            return 0
        
        # Otherwise, any split between indices 1..n-1 is valid
        return len(nums) - 1
