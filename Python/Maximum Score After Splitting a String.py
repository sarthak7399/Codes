# https://leetcode.com/problems/maximum-score-after-splitting-a-string/

# Example 1:
# Input: s = "011101"
# Output: 5 
# Explanation: 
# All possible ways of splitting s into two non-empty substrings are:
# left = "0" and right = "11101", score = 1 + 4 = 5 
# left = "01" and right = "1101", score = 1 + 3 = 4 
# left = "011" and right = "101", score = 1 + 2 = 3 
# left = "0111" and right = "01", score = 1 + 1 = 2 
# left = "01110" and right = "1", score = 2 + 1 = 3

class Solution:
    def maxScore(self, s: str) -> int:
        count0s, result = 0, -1  # Initialize counts and result variable
        total1s = s.count("1")  # Count the total number of '1's in the string
        print(total1s)  # Print the count of '1's (for debugging)
        
        # Iterate through the string except the last character
        for i in range(len(s) - 1):
            total = 0  # Initialize total score for this iteration
            num = s[i]  # Get the current character from the string
            if num == "0":  # If the character is '0'
                count0s += 1  # Increment the count of '0's
                total += (count0s + total1s)  # Update the total score
            else:  # If the character is '1'
                total1s -= 1  # Decrease the count of '1's
                total += (count0s + total1s)  # Update the total score

            result = max(total, result)  # Track the maximum score

        return result  # Return the maximum score
