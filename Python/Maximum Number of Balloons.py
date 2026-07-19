# https://leetcode.com/problems/maximum-number-of-balloons/

# Example 1:
# Input: text = "nlaebolko"
# Output: 1

class Solution:
    def maxNumberOfBalloons(self, text):
        # Convert string to a list so characters can be marked as used
        text = list(text)

        # Stores the number of times "balloon" can be formed
        ans = 0

        # Keep trying to form the word "balloon"
        while True:

            # Characters required for one occurrence of "balloon"
            word = list("balloon")

            # Try to find each required character
            for c in word:

                found = False

                # Search for the character in the remaining text
                for i in range(len(text)):

                    if text[i] == c:

                        # Mark character as used
                        text[i] = '#'

                        found = True
                        break

                # If any required character is missing,
                # we cannot form another "balloon"
                if not found:
                    return ans

            # Successfully formed one "balloon"
            ans += 1