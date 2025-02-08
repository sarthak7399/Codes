# https://leetcode.com/problems/design-a-number-container-system/

# Example 1:
# Input
# ["NumberContainers", "find", "change", "change", "change", "change", "find", "change", "find"]
# [[], [10], [2, 10], [1, 10], [3, 10], [5, 10], [10], [1, 20], [10]]
# Output
# [null, -1, null, null, null, null, 1, null, 2]

from collections import defaultdict
from heapq import heappush, heappop

class NumberContainers:
    def __init__(self):
        self.mp = {}  # Stores index -> number mapping
        self.idx = defaultdict(list)  # Min-heap for each number's indices

    def change(self, index: int, number: int) -> None:
        """ Updates the mapping and pushes the index into the heap. """
        self.mp[index] = number
        heappush(self.idx[number], index)

    def find(self, number: int) -> int:
        """ Returns the smallest index containing 'number', or -1 if not found. """
        if number not in self.idx:
            return -1
        while self.idx[number]:  # Clean up outdated indices
            i = self.idx[number][0]
            if self.mp[i] == number:
                return i
            heappop(self.idx[number])
        return -1
