# https://leetcode.com/problems/the-number-of-beautiful-subsets/

# Example 1:
# Input: nums = [2,4,6], k = 2
# Output: 4
# Explanation: The beautiful subsets of the array nums are: [2], [4], [6], [2, 6].
# It can be proved that there are only 4 beautiful subsets in the array [2,4,6].

from collections import defaultdict
from typing import List
class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        count = 0
        length_of_nums = len(nums)  # Length of the input list nums

        def explore(index):
            nonlocal count  # Access the count variable from the outer scope
            if length_of_nums == index:
                count += 1  # Increment count when all elements have been visited
                return

            num = nums[index]  # Current number being explored

            # Check if num - k and num + k have not been visited before
            if num - k not in visited and num + k not in visited:
                visited[num] += 1  # Mark num as visited
                explore(index + 1)  # Explore the next index
                visited[num] -= 1  # Backtrack: remove num from visited
                if visited[num] == 0:
                    del visited[num]  # Remove num from visited if its count becomes zero

            explore(index + 1)  # Explore the next index without including num

        visited = defaultdict(int)  # Dictionary to keep track of visited numbers and their counts
        explore(0)  # Start exploration from index 0
        return count - 1  # Subtract 1 to exclude the empty subset
