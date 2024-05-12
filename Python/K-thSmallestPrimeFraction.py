# https://leetcode.com/problems/k-th-smallest-prime-fraction/

# Example 1:
# Input: arr = [1,2,3,5], k = 3
# Output: [2,5]
# Explanation: The fractions to be considered in sorted order are:
# 1/5, 1/3, 2/5, 1/2, 3/5, and 2/3.
# The third fraction is 2/5.

# Time Complexity: O(Nlog(N)), Space Complexity: O(1)
from typing import List
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        # Length of the array
        n = len(arr)
        
        # Initialize the range for binary search
        left, right = 0, 1
        
        # Initialize result list
        result = []

        # Binary search loop
        while left <= right:
            # Calculate mid
            mid = left + (right - left) / 2
            
            # Initialize variables for this iteration
            j, total, numerator, denominator = 1, 0, 0, 0
            max_fraction = 0
            
            # Iterate through the array
            for i in range(n):
                # Find the number of elements satisfying the condition
                while j < n and arr[i] >= arr[j] * mid: # This condition means number chosen is less than the denominator and greater than the fraction 
                    j += 1
                
                # Update the total count
                total += n - j

                # Update the maximum fraction if applicable
                if j < n and max_fraction < arr[i] * 1.0 / arr[j]:  # This condition means number chosen is less than the denominator and greater than the fraction
                    max_fraction = arr[i] * 1.0 / arr[j]
                    numerator, denominator = i, j

            # Check if the total count matches k
            if total == k:
                result = [arr[numerator], arr[denominator]]
                break

            # Adjust the search range based on the total count
            if total > k:
                right = mid
            else:
                left = mid

        # Return the result
        return result
