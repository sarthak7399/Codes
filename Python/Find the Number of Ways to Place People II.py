# https://leetcode.com/problems/find-the-number-of-ways-to-place-people-ii/

# Example 1:
# Input: points = [[1,1],[2,2],[3,3]]
# Output: 0
# Explanation: There is no way to place Alice and Bob such that Alice can build a fence with Alice's position as the upper left corner and Bob's position as the lower right corner. Hence we return 0.

# # Method 1: Brute Force - Time Complexity O(N^3), Space Complexity O(N) 

# from typing import List

# class Solution:
#     def numberOfPairs(self, points: List[List[int]]) -> int:
#         n = len(points)
#         cnt = 0
#         points.sort()  # sort by x (ascending), then by y (ascending)

#         # Dictionaries to count how many points share the same x or same y
#         mpx, mpy = {}, {}
#         for x, y in points:
#             mpx[x] = mpx.get(x, 0) + 1
#             mpy[y] = mpy.get(y, 0) + 1

#         # Step 1: Check all pairs of distinct points
#         for i in range(n):
#             for j in range(i + 1, n):
#                 p1, p2 = points[i], points[j]

#                 # Skip if p2 is strictly up-right of p1 (increasing both x and y)
#                 # This pair cannot form a valid rectangle
#                 if p1[0] < p2[0] and p1[1] < p2[1]:
#                     continue

#                 # Skip if they share the same x or the same y
#                 # because we only want diagonal pairs (not aligned horizontally/vertically)
#                 if p1[0] == p2[0] or p1[1] == p2[1]:
#                     continue

#                 # Step 2: Ensure no "blocking" point lies inside the rectangle
#                 check = True
#                 for k in range(n):
#                     if k == i or k == j:
#                         continue
#                     px, py = points[k]

#                     # If this point lies strictly inside the rectangle formed by p1 and p2,
#                     # then the pair (p1, p2) is invalid
#                     if px >= p1[0] and px <= p2[0] and py >= p2[1] and py <= p1[1]:
#                         check = False
#                         break

#                 # If no blocking point found, count this pair
#                 if check:
#                     cnt += 1

#         # Step 3: Add pairs formed by multiple points with the same x or same y
#         #   - For each vertical line (same x), (val - 1) additional pairs
#         #   - For each horizontal line (same y), (val - 1) additional pairs
#         for val in mpx.values():
#             cnt += val - 1
#         for val in mpy.values():
#             cnt += val - 1

#         return cnt


# Method 2: Greedy - Time Complexity O(N^2), Space Complexity O(N)

from typing import List

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 1:
            return 0

        # ✅ Step 1: Sort points by x ascending, and if tie, by y descending
        # Why? → ensures that for same x, the higher y comes first
        # This avoids counting invalid "nested" rectangles later.
        points.sort(key=lambda p: (p[0], -p[1]))

        count = 0
        # ✅ Step 2: For each point[i], try pairing with later points[j]
        for i in range(n):
            max_y = float('-inf')   # track the best (highest so far) candidate y
            for j in range(i + 1, n):
                # We only consider point[j] if it lies below point[i]
                if points[j][1] <= points[i][1]:
                    # If this point is strictly above all previously seen y’s
                    # in this i → j scan, it forms a valid pair
                    if points[j][1] > max_y:
                        count += 1
                    # Update max_y (maintain the top boundary of the rectangle)
                    max_y = max(max_y, points[j][1])

        return count
