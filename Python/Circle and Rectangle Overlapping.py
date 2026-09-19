# https://leetcode.com/problems/circle-and-rectangle-overlapping/

# Example 1:
# Input: radius = 1, xCenter = 0, yCenter = 0, x1 = 1, y1 = -1, x2 = 3, y2 = 1
# Output: true
# Explanation: Circle and rectangle share the point (1,0).

class Solution:
    def checkOverlap(self, radius, xCenter, yCenter, x1, y1, x2, y2):

        # Find the point inside the rectangle that is closest
        # to the centre of the circle.
        #
        # If the circle's centre is horizontally inside the rectangle,
        # xCenter itself is used; otherwise, the nearest boundary is used.
        closestX = max(x1, min(xCenter, x2))
        closestY = max(y1, min(yCenter, y2))

        # Calculate the horizontal and vertical distance
        # between the circle's centre and the closest point.
        dx = xCenter - closestX
        dy = yCenter - closestY

        # Compare the squared distance with the squared radius.
        # If distance <= radius, the circle and rectangle overlap.
        #
        # Squared values are used to avoid calculating the square root.
        return dx * dx + dy * dy <= radius * radius