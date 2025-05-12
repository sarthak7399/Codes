# https://leetcode.com/problems/finding-3-digit-even-numbers/

# Example 1:
# Input: digits = [2,1,3,0]
# Output: [102,120,130,132,210,230,302,310,312,320]
# Explanation: All the possible integers that follow the requirements are in the output array. 
# Notice that there are no odd integers or integers with leading zeros.

from collections import Counter
from typing import List

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        # Count the frequency of each digit in the input list
        freq = Counter(digits)
        ans = []

        # Iterate through all 3-digit even numbers (range starts from 100 and ends at 998, step 2 ensures even)
        for x in range(100, 1000, 2):
            x0, x1, x2 = x % 10, (x // 10) % 10, x // 100  # Extract digits: units, tens, hundreds

            # Decrease the frequency of digits used in number x
            freq[x0] -= 1
            freq[x1] -= 1
            freq[x2] -= 1

            # Check if after using these digits, all frequencies are non-negative
            if freq[x0] >= 0 and freq[x1] >= 0 and freq[x2] >= 0:
                ans.append(x)  # Valid number, add to result

            # Restore frequencies back after the check
            freq[x0] += 1
            freq[x1] += 1
            freq[x2] += 1

        return ans  # Return the list of valid 3-digit even numbers
