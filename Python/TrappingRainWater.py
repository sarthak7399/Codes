# https://leetcode.com/problems/trapping-rain-water/description/

# Example 1:
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        # Initialize variables
        i = 0
        left_max = height[0]  # Initialize left maximum height
        sum = 0  # Initialize total trapped water
        j = len(height) - 1
        right_max = height[j]  # Initialize right maximum height

        while i < j:
            # If left maximum height is less than or equal to right maximum height
            if left_max <= right_max:
                sum += left_max - height[i]  # Add trapped water between current height and left maximum height
                i += 1  # Move to the next index
                left_max = max(left_max, height[i])  # Update left maximum height
            else:  # If right maximum height is greater
                sum += right_max - height[j]  # Add trapped water between current height and right maximum height
                j -= 1  # Move to the previous index
                right_max = max(right_max, height[j])  # Update right maximum height
        
        return sum  # Return the total trapped water
