# https://leetcode.com/problems/sum-of-distances/

# Example 1:
# Input: nums = [1,3,1,1,2]
# Output: [5,0,3,4,0]
# Explanation: 
# When i = 0, nums[0] == nums[2] and nums[0] == nums[3]. Therefore, arr[0] = |0 - 2| + |0 - 3| = 5. 
# When i = 1, arr[1] = 0 because there is no other index with value 3.
# When i = 2, nums[2] == nums[0] and nums[2] == nums[3]. Therefore, arr[2] = |2 - 0| + |2 - 3| = 3. 
# When i = 3, nums[3] == nums[0] and nums[3] == nums[2]. Therefore, arr[3] = |3 - 0| + |3 - 2| = 4. 
# When i = 4, arr[4] = 0 because there is no other index with value 2.

from collections import defaultdict
from typing import List
import numpy as np

# Method 1 : Time Complexity O(N), Space Complexity O(N)
class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Result array (stores sum of distances for each index)
        res = np.zeros(n, dtype=np.int64)

        # Convert input list to NumPy array for vectorized operations
        nums_arr = np.array(nums)
        
        # 1. Coordinate Manifold Transformation
        # Sort indices based on values in nums
        idx_map = np.argsort(nums_arr)

        # Sorted values of nums
        sorted_nums = nums_arr[idx_map]
        
        # 2. Segment Discovery
        # Find boundaries where value changes (i.e., different groups)
        diffs = np.where(np.diff(sorted_nums) != 0)[0] + 1

        # Start indices of each group
        starts = np.concatenate(([0], diffs))

        # End indices of each group
        ends = np.concatenate((diffs, [n]))
        
        # 3. Process each group of equal values
        for s, e in zip(starts, ends):
            # Skip groups with only one element (distance = 0)
            if e - s <= 1:
                continue
            
            # Original indices of this group
            group_idx = idx_map[s:e]

            # Sort indices to maintain increasing order of positions
            sort_order = np.argsort(group_idx)
            group_coords = group_idx[sort_order].astype(np.int64)
            
            # Prefix sum of indices (used to compute distances efficiently)
            prefix = np.cumsum(group_coords)

            # Total sum of indices in this group
            total_sum = prefix[-1]

            # Number of elements in group
            count = e - s
            
            # 4. Projection Logic (split into left and right contributions)

            # Sum of indices to the left of each position
            left_sums = np.concatenate(([0], prefix[:-1]))

            # Sum of indices to the right of each position
            right_sums = total_sum - prefix
            
            # Count of elements to the left
            left_counts = np.arange(count, dtype=np.int64)

            # Count of elements to the right
            right_counts = (count - 1) - left_counts
            
            # 5. Compute total distance:
            # Distance = sum of (current - left elements) + sum of (right elements - current)
            group_res = (group_coords * left_counts - left_sums) + \
                        (right_sums - group_coords * right_counts)
            
            # Store computed distances back to result array
            res[group_coords] = group_res
            
        # Convert NumPy array back to Python list
        return res.tolist()



# # Method 2 : Time Complexity O(N), Space Complexity O(N)
# class Solution:
#     def distance(self, nums: List[int]) -> List[int]:
#         # dist[num] → sum of indices where 'num' appears
#         # cnt[num]  → count of occurrences of 'num'
#         # prev[num] → last index where 'num' was processed
#         dist, cnt, prev = defaultdict(int), defaultdict(int), defaultdict(int)

#         # First pass: compute total index sum and frequency for each number
#         for i, num in enumerate(nums):
#             dist[num] += i
#             cnt[num] += 1

#         arr = []  # Result array

#         # Second pass: compute distance for each index
#         for i, num in enumerate(nums):
            
#             # Adjust total distance using formula:
#             # subtract contribution of elements on the left side
#             dist[num] -= (i - prev[num]) * cnt[num]

#             # Store current total distance for this index
#             arr.append(dist[num])

#             # After processing current index:
#             # reduce count by 2 (shifting one element from right to left side)
#             cnt[num] -= 2

#             # Update last seen index
#             prev[num] = i

#         return arr