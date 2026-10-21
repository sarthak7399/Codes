# https://leetcode.com/problems/minimum-operations-to-sort-a-string/

# Example 1:
# Input: s = "dog"
# Output: 1
# Explanation:​​​​​​
# Sort substring "og" to "go".
# Now, s = "dgo", which is sorted in ascending order. Thus, the answer is 1.

class Solution:
    def minOperations(self, s: str) -> int:
        # Length of the string.
        n = len(s)

        # If the string is already sorted in non-decreasing order,
        # no operations are needed.
        if all(s[i] <= s[i + 1] for i in range(n - 1)):
            return 0

        # A string of length 2 cannot be sorted using the allowed
        # operation if it is not already sorted.
        if n == 2:
            return -1

        # Find the minimum and maximum characters in the string.
        mn = min(s)
        mx = max(s)

        # If the first character is the minimum or the last character
        # is the maximum, the string can be sorted in one operation.
        if s[0] == mn or s[-1] == mx:
            return 1

        # If the minimum or maximum character appears in the middle,
        # two operations are sufficient.
        if any(c == mn or c == mx for c in s[1:-1]):
            return 2

        # Otherwise, three operations are required.
        return 3