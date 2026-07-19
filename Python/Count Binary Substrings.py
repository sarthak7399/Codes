# https://leetcode.com/problems/count-binary-substrings/

# Example 1:
# Input: s = "00110011"
# Output: 6
# Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".
# Notice that some of these substrings repeat and are counted the number of times they occur.
# Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # c       → length of current continuous group (000 or 111)
        # prev_c  → length of previous group
        # res     → total valid substrings count
        c = prev_c = res = 0
        
        # stores previous character to detect group change
        prev_ch = '~'   # dummy initial value
        
        for ch in s:
            # If same character continues → extend current group
            if prev_ch == ch:
                c += 1
            else:
                # Group changed (0→1 or 1→0)
                # Number of valid substrings formed between
                # previous and current group is:
                # min(previous group size, current group size)
                res += min(prev_c, c)

                # Shift current group to previous
                prev_c = c

                # Start new group
                c = 1
                prev_ch = ch
        
        # Add result for the last pair of groups
        res += min(prev_c, c)

        return res
