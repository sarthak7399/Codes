# https://leetcode.com/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros/

# Example 1:
# Input: nums1 = [3,2,0,1,0], nums2 = [6,5,0]
# Output: 12
# Explanation: We can replace 0's in the following way:
# - Replace the two 0's in nums1 with the values 2 and 4. The resulting array is nums1 = [3,2,2,1,4].
# - Replace the 0 in nums2 with the value 1. The resulting array is nums2 = [6,5,1].
# Both arrays have an equal sum of 12. It can be shown that it is the minimum sum we can obtain.

class Solution:
    def minSum(self, nums1, nums2):
        # Replace each 0 with 1 (minimum possible positive integer)
        # Then compute the total sum for both arrays
        nums1_sum = sum(x if x != 0 else 1 for x in nums1)
        nums2_sum = sum(x if x != 0 else 1 for x in nums2)

        # Count number of zeros in both arrays
        nums1_zeros = nums1.count(0)
        nums2_zeros = nums2.count(0)

        # If one array has no zeros and its sum is strictly less than the other (which can still be increased by zeros),
        # then it is impossible to make the two arrays equal by replacing zeros with positive integers (≥1)
        if (nums1_zeros == 0 and nums2_sum > nums1_sum) or \
           (nums2_zeros == 0 and nums1_sum > nums2_sum):
            return -1

        # Otherwise, return the maximum of the two sums (this is the minimal common sum we can make)
        return max(nums1_sum, nums2_sum)
