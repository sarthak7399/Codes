# https://leetcode.com/problems/take-k-of-each-character-from-left-and-right/

# Example 1:
# Input: s = "aabaaaacaabc", k = 2
# Output: 8
# Explanation: 
# Take three characters from the left of s. You now have two 'a' characters, and one 'b' character.
# Take five characters from the right of s. You now have four 'a' characters, two 'b' characters, and two 'c' characters.
# A total of 3 + 5 = 8 minutes is needed.
# It can be proven that 8 is the minimum number of minutes needed.

class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        # Step 1: Initialize frequency counts for 'a', 'b', and 'c'
        freqs = [0] * 3  # freqs[0] = count of 'a', freqs[1] = count of 'b', freqs[2] = count of 'c'
        n = len(s)  # Length of the input string
        
        # Step 2: Count the frequency of each character in the string
        for c in s:
            freqs[ord(c) - ord('a')] += 1  # Map 'a', 'b', 'c' to indices 0, 1, 2
        
        # Step 3: Check if it's possible to have at least k of each character
        if freqs[0] < k or freqs[1] < k or freqs[2] < k:
            return -1  # If any character has fewer than k occurrences, it's impossible
        
        # Step 4: Initialize two pointers and start shrinking the window from the right
        i = 0  # Start of the sliding window
        for j in range(n):  # End of the sliding window
            # Reduce the count of the character at index j
            freqs[ord(s[j]) - ord('a')] -= 1
            
            # If removing this character makes any frequency less than k, move the left pointer
            if freqs[0] < k or freqs[1] < k or freqs[2] < k:
                # Restore the count for the character at index i and move the left pointer
                freqs[ord(s[i]) - ord('a')] += 1
                i += 1
        
        # Step 5: Calculate the minimum number of characters to take
        return n - (j - i + 1)  # The smallest valid window is removed, so subtract its size from total
