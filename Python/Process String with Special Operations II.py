# https://leetcode.com/problems/process-string-with-special-operations-ii/

# Example 1:
# Input: s = "a#b%*", k = 1
# Output: "a"
# Explanation:
# i	s[i]	Operation	Current result
# 0	'a'	Append 'a'	"a"
# 1	'#'	Duplicate result	"aa"
# 2	'b'	Append 'b'	"aab"
# 3	'%'	Reverse result	"baa"
# 4	'*'	Remove the last character	"ba"
# The final result is "ba". The character at index k = 1 is 'a'.

class Solution:
    def processStr(self, s: str, k: int) -> str:
        # Stores the length of the final processed string
        length = 0

        # --------------------------------------------------
        # Step 1: Compute the final string length without
        # actually building the string
        # --------------------------------------------------
        for c in s:

            # Backspace operation
            if c == '*':
                length = max(0, length - 1)

            # Duplicate the current string
            elif c == '#':
                length *= 2

            # '%' reverses the string, so length remains unchanged
            elif c != '%':
                length += 1

        # If k is outside the final string range
        if k >= length:
            return '.'

        # --------------------------------------------------
        # Step 2: Walk backwards through the operations
        # and trace which original character ends up at
        # position k
        # --------------------------------------------------
        for i in range(len(s) - 1, -1, -1):

            c = s[i]

            # Reverse effect of '*'
            # Before deletion, string length was one larger
            if c == '*':
                length += 1

            # Reverse effect of '#'
            elif c == '#':

                # Before duplication, string length was half
                half = length // 2

                # If k is in the duplicated second half,
                # map it back to the corresponding position
                # in the first half
                if k >= half:
                    k -= half

                length = half

            # Reverse effect of '%'
            elif c == '%':

                # Reversal maps index k to its mirrored position
                k = length - 1 - k

            # Regular character
            else:

                # If this character occupies position k,
                # we've found the answer
                if k == length - 1:
                    return c

                # Remove this character from consideration
                length -= 1

        # Fallback (should not normally be reached)
        return '.'