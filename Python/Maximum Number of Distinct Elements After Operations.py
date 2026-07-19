# https://leetcode.com/problems/maximum-number-of-distinct-elements-after-operations/

# Example 1:
# Input: nums = [1,2,2,3,3,4], k = 2
# Output: 6
# Explanation:
# nums changes to [-1, 0, 1, 2, 3, 4] after performing operations on the first four elements.

class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        nums.sort()  # sort numbers to process in increasing order
        count = 0    # count of distinct elements formed
        prev = -(1 << 30)  # track last chosen element (very small initially)

        for a in nums:
            low = a - k      # minimum value allowed for this element
            high = a + k     # maximum value allowed for this element
            x = prev + 1     # pick next distinct value greater than previous
            if x < low:      # ensure within lower bound
                x = low
            if x <= high:    # valid pick within allowed range
                count += 1
                prev = x     # update previous chosen element
        return count
