# https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/

# Example 1:
# Input: arr1 = [1,10,100], arr2 = [1000]
# Output: 3
# Explanation: There are 3 pairs (arr1[i], arr2[j]):
# - The longest common prefix of (1, 1000) is 1.
# - The longest common prefix of (10, 1000) is 10.
# - The longest common prefix of (100, 1000) is 100.
# The longest common prefix is 100 with a length of 3.

from typing import List

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        X, Y = len(arr1), len(arr2)  # lengths (not directly used later)

        s = set()  # stores all prefixes of numbers in arr2

        # Generate all numeric prefixes for arr2 elements
        for i in arr2:
            copy = i

            # Example: 12345 → 12345, 1234, 123, 12, 1
            s.add(copy)

            # Keep removing last digit to form prefixes
            copy = copy // 10
            while copy > 0:
                s.add(copy)
                copy = copy // 10

        t = set()  # stores all prefixes of numbers in arr1

        # Generate all numeric prefixes for arr1 elements
        for i in arr1:
            copy = i

            # Example: 12345 → 12345, 1234, 123, 12, 1
            t.add(copy)

            # Keep removing last digit to form prefixes
            copy = copy // 10
            while copy > 0:
                t.add(copy)
                copy = copy // 10

        ans = 0  # stores maximum common prefix length

        # Compare prefixes of arr1 and arr2
        for i in t:
            if i in s:
                # length of number gives prefix length
                ans = max(ans, len(str(i)))

        return ans