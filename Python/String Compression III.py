# https://leetcode.com/problems/string-compression-iii/

# Example 2:
# Input: word = "aaaaaaaaaaaaaabb"
# Output: "9a5a2b"
# Explanation:
# Initially, comp = "". Apply the operation 3 times, choosing "aaaaaaaaa", "aaaaa", and "bb" as the prefix in each operation.
# For prefix "aaaaaaaaa", append "9" followed by "a" to comp.
# For prefix "aaaaa", append "5" followed by "a" to comp.
# For prefix "bb", append "2" followed by "b" to comp.

class Solution:
    def compressedString(self, word: str) -> str:
        # Initialize the result string and the count
        compressed_result = ""
        count = 1

        # Edge case: empty string
        if len(word) == 0:
            return compressed_result

        # Traverse the word except for the last character
        for i in range(1, len(word)):
            # If the current character is the same as the previous, increment the count
            if word[i] == word[i - 1]:
                count += 1
            else:
                # Process the previous sequence if it reached the end of a run
                while count > 9:
                    compressed_result += "9" + word[i - 1]
                    count -= 9
                # Append remaining count for the sequence
                if count > 0:
                    compressed_result += str(count) + word[i - 1]
                # Reset count for the new character
                count = 1

        # Append the last sequence after loop ends
        while count > 9:
            compressed_result += "9" + word[-1]
            count -= 9
        if count > 0:
            compressed_result += str(count) + word[-1]

        return compressed_result
