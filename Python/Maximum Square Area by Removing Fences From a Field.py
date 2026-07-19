# https://leetcode.com/problems/maximum-square-area-by-removing-fences-from-a-field/

# Example 1:
# Input: m = 4, n = 3, hFences = [2,3], vFences = [2]
# Output: 4
# Explanation: Removing the horizontal fence at 2 and the vertical fence at 2 will give a square field of area 4.

class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        hdiffs = set()

        # Add boundary fences and sort
        hFences.append(1)
        hFences.append(m)
        hFences.sort()

        # Store all possible horizontal distances
        for i in range(len(hFences)):
            hi = hFences[i]
            for j in range(i + 1, len(hFences)):
                hdiffs.add(hFences[j] - hi)

        mx = 0

        # Add boundary fences and sort
        vFences.append(1)
        vFences.append(n)
        vFences.sort()

        # Find largest vertical distance that also exists horizontally
        for i in range(len(vFences)):
            vi = vFences[i]
            for j in range(i + 1, len(vFences)):
                diff = vFences[j] - vi
                if diff > mx and diff in hdiffs:
                    mx = diff

        # Return area or -1 if no square is possible
        return (mx * mx) % (10**9 + 7) if mx != 0 else -1
