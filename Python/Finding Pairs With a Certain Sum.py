# https://leetcode.com/problems/finding-pairs-with-a-certain-sum/

# Example 1:
# Input
# ["FindSumPairs", "count", "add", "count", "count", "add", "add", "count"]
# [[[1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4]], [7], [3, 2], [8], [4], [0, 1], [1, 1], [7]]
# Output
# [null, 8, null, 2, 1, null, null, 11]
# Explanation
# FindSumPairs findSumPairs = new FindSumPairs([1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4]);
# findSumPairs.count(7);  // return 8; pairs (2,2), (3,2), (4,2), (2,4), (3,4), (4,4) make 2 + 5 and pairs (5,1), (5,5) make 3 + 4
# findSumPairs.add(3, 2); // now nums2 = [1,4,5,4,5,4]
# findSumPairs.count(8);  // return 2; pairs (5,2), (5,4) make 3 + 5
# findSumPairs.count(4);  // return 1; pair (5,0) makes 3 + 1
# findSumPairs.add(0, 1); // now nums2 = [2,4,5,4,5,4]
# findSumPairs.add(1, 1); // now nums2 = [2,5,5,4,5,4]
# findSumPairs.count(7);  // return 11; pairs (2,1), (2,2), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,4) make 2 + 5 and pairs (5,3), (5,5) make 3 + 4

from collections import defaultdict
from typing import List

class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        # Store frequency of elements in nums1
        self.dic = defaultdict(int)
        for num in nums1:
            self.dic[num] += 1
        
        # Store elements of nums2 in a list (so it can be updated)
        self.arr = [num for num in nums2]

        # Store frequency of elements in nums2
        self.dic2 = defaultdict(int)
        for num in nums2:
            self.dic2[num] += 1

    def add(self, index: int, val: int) -> None:
        # Get the current value at index in nums2
        old = self.arr[index]

        # Update the value at the given index
        self.arr[index] += val

        # Update the frequency map for nums2
        self.dic2[old] -= 1
        self.dic2[self.arr[index]] += 1

    def count(self, tot: int) -> int:
        ans = 0
        # Iterate over all values in nums1's frequency dictionary
        for num1 in self.dic:
            # Check if the complement (tot - num1) exists in nums2's frequency map
            complement = tot - num1
            if complement in self.dic2:
                # Multiply the frequencies from both sides and add to result
                ans += self.dic[num1] * self.dic2[complement]
        return ans
