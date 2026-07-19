# https://leetcode.com/problems/words-within-two-edits-of-dictionary/

# Example 1:
# Input: queries = ["word","note","ants","wood"], dictionary = ["wood","joke","moat"]
# Output: ["word","note","wood"]
# Explanation:
# - Changing the 'r' in "word" to 'o' allows it to equal the dictionary word "wood".
# - Changing the 'n' to 'j' and the 't' to 'k' in "note" changes it to "joke".
# - It would take more than 2 edits for "ants" to equal a dictionary word.
# - "wood" can remain unchanged (0 edits) and match the corresponding dictionary word.
# Thus, we return ["word","note","wood"].

from typing import List

class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        ans = []  # List to store valid query words

        # Iterate over each query word
        for q in queries:

            # Compare with each word in dictionary
            for d in dictionary:
                diff = 0  # Count number of differing characters

                # Compare characters at each position
                for i in range(len(q)):
                    if q[i] != d[i]:
                        diff += 1  # Increment difference count

                    # If more than 2 differences, stop early
                    if diff > 2:
                        break

                # If differences are within allowed limit (≤ 2)
                if diff <= 2:
                    ans.append(q)  # Add query to result
                    break  # No need to check further dictionary words

        return ans  # Return all valid queries