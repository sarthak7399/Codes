# https://leetcode.com/problems/construct-smallest-number-from-di-string/

# Example 1:
# Input: pattern = "IIIDIDDD"
# Output: "123549876"
# Explanation:
# At indices 0, 1, 2, and 4 we must have that num[i] < num[i+1].
# At indices 3, 5, 6, and 7 we must have that num[i] > num[i+1].
# Some possible values of num are "245639871", "135749862", and "123849765".
# It can be proven that "123549876" is the smallest possible num that meets the conditions.
# Note that "123414321" is not possible because the digit '1' is used more than once.

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)  # Length of the pattern
        result = ""  # To store the final result
        stack = []  # Stack to hold numbers temporarily
        
        for i in range(n + 1):
            stack.append(i + 1)  # Push the next number to the stack
            
            # If 'I' is found or it's the end of the pattern, pop from stack
            if i == n or pattern[i] == 'I':
                while stack:
                    result += str(stack.pop())  # Pop from the stack and add to result
        
        return result  # Return the final result
