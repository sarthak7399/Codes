# https://leetcode.com/problems/construct-uniform-parity-array-i/

# Example 1:
# Input: nums1 = [2,3]
# Output: true
# Explanation:
# Choose nums2[0] = nums1[0] - nums1[1] = 2 - 3 = -1.
# Choose nums2[1] = nums1[1] = 3.
# nums2 = [-1, 3], and both elements are odd. Thus, the answer is true​​​​​​​.

class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        # Count the number of even and odd elements.
        odd = 0
        even = 0
        n = len(nums1)

        for i in nums1:
            # Increment the corresponding parity count.
            if i % 2 == 0:
                even += 1
            else:
                odd += 1

        # If all elements have the same parity, the array is uniform.
        if even == n or odd == n:
            return True

        # If the array contains both even and odd elements,
        # it is also considered valid according to the condition.
        elif even >= 1 and odd >= 1:
            return True

        # Return False otherwise.
        return False