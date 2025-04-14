# https://leetcode.com/problems/count-good-triplets/

# Example 1:
# Input: arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3
# Output: 4
# Explanation: There are 4 good triplets: [(3,0,1), (3,0,1), (3,1,1), (0,1,1)].

from typing import List
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        good_triplets = 0
        length = len(arr)

        for i in range(length):  # i is the first index
            for j in range(i + 1, length):  # j must be after i
                if abs(arr[i] - arr[j]) <= a:  # first condition check
                    for k in range(j + 1, length):  # k must be after j
                        # Check all three conditions
                        if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                            good_triplets += 1
        
        return good_triplets