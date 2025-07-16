# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/

# Example 1:
# Input: tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]
# Output: 2
# Explanation: 
# The first figure represents the dominoes as given by tops and bottoms: before we do any rotations.
# If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.

class Solution(object):
    def minDominoRotations(self, tops, bottoms):
        # Try to make all dominos show tops[0] or bottoms[0] on either top or bottom
        # Start with the value in tops[0] as the candidate target
        res = self.getRotation(tops, bottoms, tops[0])

        # If bottoms[0] is different, check if making everything equal to bottoms[0] is better
        if bottoms[0] != tops[0]:
            res = min(res, self.getRotation(tops, bottoms, bottoms[0]))

        # If it was impossible to align all values to any target, return -1
        return -1 if res == float('inf') else res

    def getRotation(self, tops, bottoms, target):
        rotateTop = 0       # Count of rotations needed to make all tops equal to target
        rotateBottom = 0    # Count of rotations needed to make all bottoms equal to target

        for i in range(len(tops)):
            # If neither top nor bottom has the target number, it's impossible for this domino
            if tops[i] != target and bottoms[i] != target:
                return float('inf')

            # If the top doesn't match the target, we would need to rotate this domino
            if tops[i] != target:
                rotateTop += 1

            # If the bottom doesn't match the target, we would need to rotate this domino
            if bottoms[i] != target:
                rotateBottom += 1

        # Return the minimum number of rotations required (either all tops or all bottoms)
        return min(rotateTop, rotateBottom)
