# https://leetcode.com/problems/subarray-product-less-than-k/description/?envType=daily-question&envId=2024-03-15

# Example 1:
# Input: nums = [10,5,2,6], k = 100
# Output: 8
# Explanation: The 8 subarrays that have product less than 100 are:
# [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
# Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.


from typing import List
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:   # Check if k is less than or equal to 1
            return 0

        left, right, product, count = 0, 0, 1, 0  # Initialize pointers, product, and count
        n = len(nums)  # Get the length of the input array

        while right < n:  # Iterate until the right pointer reaches the end of the array
            product *= nums[right]  # Update the product by multiplying with the current element
            while product >= k:  # Shrink the window if product is greater than or equal to k
                product //= nums[left]  # Divide product by the element at the left pointer
                left += 1  # Move the left pointer to the right
            count += 1 + (right - left)  # Increment count by the number of subarrays within the window
            right += 1  # Move the right pointer to the right

        return count  # Return the total count of subarrays
