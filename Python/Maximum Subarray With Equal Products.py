# https://leetcode.com/problems/maximum-subarray-with-equal-products/

# Example 1:
# Input: nums = [1,2,1,2,1,1,1]
# Output: 5
# Explanation: 
# The longest product equivalent subarray is [1, 2, 1, 1, 1], where prod([1, 2, 1, 1, 1]) = 2, gcd([1, 2, 1, 1, 1]) = 1, and lcm([1, 2, 1, 1, 1]) = 2.

from typing import List

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        # Try every possible starting index of the subarray
        for i in range(n):
            prod = 1  # Product of elements in the current subarray
            g = 0    # GCD of elements in the current subarray
            lc = 1   # LCM of elements in the current subarray

            # Extend the subarray by adding elements one by one
            for j in range(i, n):
                x = nums[j]

                # Update GCD of the current subarray
                if g == 0:
                    g = x
                else:
                    # Calculate GCD using the Euclidean algorithm
                    a, b = g, x
                    while b:
                        a, b = b, a % b
                    g = a

                # Calculate GCD of the current LCM and the new element
                gg, b = lc, x
                while b:
                    gg, b = b, gg % b

                # Check for potential LCM overflow before multiplication
                if lc // gg > (10**18) // x:
                    break

                # Update LCM using the formula:
                # LCM(a, b) = (a // GCD(a, b)) * b
                lc = lc // gg * x

                # Check for potential product overflow before multiplication
                if prod > (10**18) // x:
                    break

                # Update the product of the current subarray
                prod *= x

                # Check whether product = GCD * LCM
                if prod == lc * g:
                    # Update the maximum valid subarray length
                    ans = max(ans, j - i + 1)

        # Return the maximum length found
        return ans