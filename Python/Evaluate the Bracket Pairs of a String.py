# https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/

# Example 1:
# Input: s = "(name)is(age)yearsold", knowledge = [["name","bob"],["age","two"]]
# Output: "bobistwoyearsold"
# Explanation:
# The key "name" has a value of "bob", so replace "(name)" with "bob".
# The key "age" has a value of "two", so replace "(age)" with "two".

class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        # Create a dictionary for quick key-value lookup.
        mp = {k: v for k, v in knowledge}

        # Store the final evaluated string characters.
        res = []

        # Length of the input string.
        n = len(s)

        # Pointer to traverse the string.
        i = 0

        while i < n:
            # If we find '(', a key starts here.
            if s[i] == '(':
                # Start searching for the closing ')'.
                j = i + 1

                # Find the end of the key.
                while s[j] != ')':
                    j += 1

                # Extract the key between '(' and ')'.
                key = s[i + 1:j]

                # Add the corresponding value.
                # Use '?' if the key is not present in the dictionary.
                res.append(mp.get(key, "?"))

                # Move past the closing ')'.
                i = j + 1

            else:
                # Normal character, so add it directly.
                res.append(s[i])

                # Move to the next character.
                i += 1

        # Join all characters/values to form the final string.
        return "".join(res)