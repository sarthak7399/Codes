# https://leetcode.com/problems/remove-k-digits/description/

# Example 1:
# Input: num = "1432219", k = 3
# Output: "1219"
# Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

# Example 2:
# Input: num = "10200", k = 1
# Output: "200"
# Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # If the number of digits to remove is greater than or equal to the length of the number,
        # return "0" because all digits can be removed
        if k >= len(num):
            return "0"

        # Initialize an empty stack to store digits
        stack = []
        # Initialize a variable to keep track of the number of digits removed
        removed = 0
        
        # Iterate through each digit in the number
        for digit in num:
            # While there are digits in the stack, the current digit is smaller than the top digit in the stack,
            # and there are still digits to be removed, pop digits from the stack
            while stack and stack[-1] > digit and removed < k:
                stack.pop()
                removed += 1
            
            # Push the current digit onto the stack
            stack.append(digit)
        
        # If there are still digits to be removed, pop them from the stack
        while removed < k:
            stack.pop()
            removed += 1
        
        # Convert the stack to a string and remove leading zeros
        result = ''.join(stack).lstrip('0')
        # Return the result or "0" if the result is empty
        return result if result else "0"
