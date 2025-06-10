# https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/

# Example 1:
# Input: s = "aaaaabbc"
# Output: 3
# Explanation:
# The character 'a' has an odd frequency of 5, and 'b' has an even frequency of 2.
# The maximum difference is 5 - 2 = 3.

class Solution:
    def maxDifference(self, s: str) -> int:
        from collections import Counter
        
        # Count the frequency of each character in the string
        freq = Counter(s)

        odd = 0               # To track the maximum frequency among characters with odd counts
        even = len(s)         # To track the minimum frequency among characters with even counts

        for count in freq.values():
            if count % 2 == 1:
                # Update 'odd' with the maximum odd frequency found so far
                odd = max(odd, count)
            elif count != 0:
                # Update 'even' with the minimum even frequency found so far
                even = min(even, count)

        # Return the difference between the highest odd frequency and lowest even frequency
        return odd - even
