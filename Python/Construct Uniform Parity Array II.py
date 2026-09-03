# https://leetcode.com/problems/construct-uniform-parity-array-ii/

# Example 1:
# Input: nums1 = [1,4,7]
# Output: true
# Explanation:​​​​​​​​​​​​​​
# Set nums2[0] = nums1[0] = 1.
# Set nums2[1] = nums1[1] - nums1[0] = 4 - 1 = 3.
# Set nums2[2] = nums1[2] = 7.
# nums2 = [1, 3, 7], and all elements are odd. Thus, the answer is true.

class Solution:
    def uniformArray(self, nums):
        # Store the smallest odd number found in the array.
        smallestOdd = float('inf')

        # Find the minimum odd number.
        for num in nums:
            if num % 2 == 1:
                smallestOdd = min(smallestOdd, num)

        # If there are no odd numbers, all elements are already even,
        # so the array is considered uniform.
        if smallestOdd == float('inf'):
            return True

        # Check every even number.
        # An even number can be converted to an odd number only if
        # it is greater than the smallest odd number.
        for num in nums:
            if num % 2 == 0 and num <= smallestOdd:
                return False

        # All even numbers can be converted successfully.
        return True