# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/?envType=daily-question&envId=2024-03-15

# Example 1:
# Input: points = [[10,16],[2,8],[1,6],[7,12]]
# Output: 2
# Explanation: The balloons can be burst by 2 arrows:
# - Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
# - Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].

from typing import List
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])  # Sort the points based on their start positions 
        
        arrows = 1  # Initialize the number of arrows required to 1
        end = points[0][1]  # Initialize the end position with the end position of the first balloon
        
        # Iterate through the sorted points list starting from the second balloon
        for balloon in points[1:]:
            if balloon[0] > end:  # If the start position of the current balloon is greater than the previous end position
                arrows += 1  # Increment the arrow count
                end = balloon[1]  # Update the end position to the end position of the current balloon
            else:
                end = min(end, balloon[1])  # Otherwise, update the end position to the minimum of the current end position and the end position of the current balloon
        
        return arrows  # Return the total number of arrows required
