# https://leetcode.com/problems/weighted-word-mapping/

# Example 1:
# Input: words = ["abcd","def","xyz"], weights = [5,3,12,14,1,2,3,2,10,6,6,9,7,8,7,10,8,9,6,9,9,8,3,7,7,2]
# Output: "rij"
# Explanation:
# The weight of "abcd" is 5 + 3 + 12 + 14 = 34. The result modulo 26 is 34 % 26 = 8, which maps to 'r'.
# The weight of "def" is 14 + 1 + 2 = 17. The result modulo 26 is 17 % 26 = 17, which maps to 'i'.
# The weight of "xyz" is 7 + 7 + 2 = 16. The result modulo 26 is 16 % 26 = 16, which maps to 'j'.
# Thus, the string formed by concatenating the mapped characters is "rij".

from typing import List

class Solution:
    def mapWordWeights(self, words: List[str], wt: List[int]) -> str:
        # Stores the resulting characters
        res = []

        # Process each word independently
        for word in words:

            # Compute total weight of the current word
            s = 0

            for ch in word:
                # Convert character to 0-based alphabet index:
                # 'a'/'A' -> 0, ..., 'z'/'Z' -> 25
                #
                # (ord(ch) & 31) extracts the alphabet position
                # irrespective of case.
                s += wt[(ord(ch) & ((1 << 5) - 1)) - 1]

            # Map the accumulated weight to a character.
            #
            # ((s * 2521) >> 4) is an optimized way of computing
            # a scaled value (typically used instead of division).
            #
            # The resulting value is reduced using len(wt)
            # and converted into a lowercase character.
            res.append(
                chr(
                    122 - (
                        s
                        - ((s * 2521) >> (1 << 4)) * len(wt)
                    )
                )
            )

        # Combine all generated characters into a single string
        return "".join(res)