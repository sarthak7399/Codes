# https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii/

# Example 1:
# Input: word = "aeioqq", k = 1
# Output: 0
# Explanation:
# There is no substring with every vowel.

class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        frequencies = [{}, {}]  # First dict tracks vowels, second tracks frequency in window
        for v in "aeiou":
            frequencies[0][v] = 1  # Mark vowels in the first dictionary
        
        response, currentK, vowels, extraLeft, left = 0, 0, 0, 0, 0

        for right, rightChar in enumerate(word):
            if rightChar in frequencies[0]:  # If it's a vowel
                frequencies[1][rightChar] = frequencies[1].get(rightChar, 0) + 1
                if frequencies[1][rightChar] == 1:
                    vowels += 1
            else:
                currentK += 1  # Non-vowel characters count toward `k`

            # Shrink window if `currentK` exceeds `k`
            while currentK > k:
                leftChar = word[left]
                if leftChar in frequencies[0]:
                    frequencies[1][leftChar] -= 1
                    if frequencies[1][leftChar] == 0:
                        vowels -= 1
                else:
                    currentK -= 1
                left += 1
                extraLeft = 0  # Reset count of extra left removals

            # Adjust left boundary while keeping all vowels and required non-vowels
            while vowels == 5 and currentK == k and left < right and word[left] in frequencies[0] and frequencies[1][word[left]] > 1:
                extraLeft += 1
                frequencies[1][word[left]] -= 1
                left += 1

            # If conditions are met, add valid substrings to result
            if currentK == k and vowels == 5:
                response += (1 + extraLeft)

        return response
