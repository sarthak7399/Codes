# https://leetcode.com/problems/rectangle-overlap/

# Example 1:
# Input: rec1 = [0,0,2,2], rec2 = [1,1,3,3]
# Output: true

# Example 2:
# Input: rec1 = [0,0,1,1], rec2 = [1,0,2,1]
# Output: false

class Solution:
    def isRectangleOverlap(self, rec1, rec2):
        # Find the left boundary of the overlapping region.
        left = max(rec1[0], rec2[0])

        # Find the right boundary of the overlapping region.
        right = min(rec1[2], rec2[2])

        # Find the bottom boundary of the overlapping region.
        bottom = max(rec1[1], rec2[1])

        # Find the top boundary of the overlapping region.
        top = min(rec1[3], rec2[3])

        # Rectangles overlap only if the overlapping region
        # has a positive width and a positive height.
        #
        # Strict '<' means touching at an edge or corner
        # is not considered an overlap.
        return left < right and bottom < top