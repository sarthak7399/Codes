# https://leetcode.com/problems/container-with-most-water/

# Example 1:
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

class Solution:
    def maxArea(self, height: list[int]) -> int:
        i = 0                      # left pointer
        j = len(height) - 1        # right pointer
        res = 0                    # stores maximum area found

        # Two-pointer approach to find max water container
        while i < j:
            # Calculate area between current two lines
            res = max(res, (j - i) * min(height[i], height[j]))

            # Move the pointer pointing to the shorter line
            # (to potentially find a taller line for larger area)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return res                 # return the maximum area found
