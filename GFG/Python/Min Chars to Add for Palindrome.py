# https://www.geeksforgeeks.org/problems/minimum-characters-to-be-added-at-front-to-make-string-palindrome/

# Example 1:
# Input: s = "aacecaaaa"
# Output: 2
# Explanation: Add 2 a's at front of above string to make it palindrome : "aaaacecaaaa"

class Solution:
    def minChar(self, s):
        # Reverse the input string
        rev_s = s[::-1]
        
        # Combine the original string, a separator ('#'), and the reversed string
        # This helps in creating a new string for palindrome checking using LPS array
        combined = s + "#" + rev_s
        
        # Calculate the length of the combined string
        n = len(combined)
        
        # Initialize the LPS (Longest Prefix which is also Suffix) array
        # It helps in determining the longest palindromic prefix of the string
        lps = [0] * n
        
        # Build the LPS array for the combined string
        for i in range(1, n):
            # Start with the value from the previous position in LPS array
            j = lps[i - 1]
            
            # Adjust the index `j` until a match is found or it becomes 0
            while j > 0 and combined[i] != combined[j]:
                j = lps[j - 1]
            
            # If characters match, increase the matching length
            if combined[i] == combined[j]:
                j += 1
            
            # Update the LPS array at the current position
            lps[i] = j
        
        # The last value in the LPS array gives the length of the longest palindromic
        # prefix in the combined string. Subtract this value from the original
        # string length to get the minimum characters to be added at the front
        return len(s) - lps[-1]