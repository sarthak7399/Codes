# https://leetcode.com/problems/process-string-with-special-operations-i/

# Example 1:
# Input: s = "a#b%*"
# Output: "ba"
# Explanation:
# i	s[i]	Operation	Current result
# 0	'a'	Append 'a'	"a"
# 1	'#'	Duplicate result	"aa"
# 2	'b'	Append 'b'	"aab"
# 3	'%'	Reverse result	"baa"
# 4	'*'	Remove the last character	"ba"
# Thus, the final result is "ba".

class Solution:
    """
    Processes a string based on special commands:

    Rules:
    - Lowercase letters: Append to the result.
    - '*': Remove the last character (backspace).
    - '#': Duplicate the current result.
    - '%': Reverse the current result.

    Complexity Analysis:
    - Time: O(N * K), where N is the number of characters in the
      input string and K is the current length of the result list
      during '#' and '%' operations.
    - Space: O(N) for storing the generated result.
    """

    def processStr(self, s: str) -> str:
        # Stores the current processed characters
        result = []

        # Process each character in the input string
        for c in s:

            # Append lowercase letters to the result
            if c.islower():
                result.append(c)

            # Backspace operation:
            # remove the most recently added character
            elif c == '*':
                if result:
                    result.pop()

            # Duplicate the current result
            elif c == '#':

                # Example:
                # ['a', 'b'] -> ['a', 'b', 'a', 'b']
                result += result

            # Reverse the current result in-place
            elif c == '%':

                # Example:
                # ['a', 'b', 'c'] -> ['c', 'b', 'a']
                result.reverse()

        # Convert character list back to a string
        return "".join(result)