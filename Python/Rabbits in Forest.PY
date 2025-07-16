# https://leetcode.com/problems/rabbits-in-forest/

# Example 1:
# Input: answers = [1,1,2]
# Output: 5
# Explanation:
# The two rabbits that answered "1" could both be the same color, say red.
# The rabbit that answered "2" can't be red or the answers would be inconsistent.
# Say the rabbit that answered "2" was blue.
# Then there should be 2 other blue rabbits in the forest that didn't answer into the array.
# The smallest possible number of rabbits in the forest is therefore 5: 3 that answered plus 2 that didn't.

from collections import Counter
from math import ceil
from typing import List

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        # Count how many times each answer appears
        freq = Counter(answers)
        total = 0  # Initialize total number of rabbits

        # Iterate over each unique answer `k` and its count `v`
        for k, v in freq.items():
            group_size = k + 1  # Each rabbit that answers `k` implies a group of size `k + 1`
            
            # Calculate how many such full groups are needed
            # If we have more rabbits answering `k` than fit in a group, we need multiple groups
            groups = ceil(v / group_size)

            # Total rabbits contributed by these groups = number of groups * size of each group
            total += groups * group_size

        return total
