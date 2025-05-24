# https://leetcode.com/problems/find-words-containing-character/

# Example 1:
# Input: words = ["leet","code"], x = "e"
# Output: [0,1]
# Explanation: "e" occurs in both words: "leet", and "code". Hence, we return indices 0 and 1.

class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """

        # Step 1: Create an empty list to store the result
        result = []

        # Step 2: Loop through the list of words using index
        for i in range(len(words)):

            # Step 3: Check if the character x is present in the current word
            if x in words[i]:

                # Step 4: If yes, add the index i to the result list
                result.append(i)

        # Step 5: Return the list of indices
        return result