# https://leetcode.com/problems/separate-the-digits-in-an-array/

# Example 1:
# Input: nums = [13,25,83,77]
# Output: [1,3,2,5,8,3,7,7]
# Explanation: 
# - The separation of 13 is [1,3].
# - The separation of 25 is [2,5].
# - The separation of 83 is [8,3].
# - The separation of 77 is [7,7].
# answer = [1,3,2,5,8,3,7,7]. Note that answer contains the separations in the same order.

from typing import List

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []  # Stores separated digits

        # Traverse each number in the input list
        for i in nums:

            # Convert number to string, then to list of characters
            j = list(str(i))

            # Convert each character back to integer
            # and append to result
            for k in j:
                ans.append(int(k))

        return ans