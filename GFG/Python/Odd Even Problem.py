# https://www.geeksforgeeks.org/problems/help-nobita0532/

# Example 1:
# Input:  s = "abbbcc"
# Output:  ODD
# Explanation: 
# x = 0 and y = 1 so (x + y) is ODD. 'a' occupies 1st place(odd) in english alphabets and its frequency is odd(1), 'b' occupies 2nd place(even) but its frequency is odd(3) so it doesn't get counted and 'c' occupies 3rd place(odd) but its frequency is even(2) so it also doesn't get counted.

class Solution:
    def oddEven(self, s : str) -> str:
        # Step 1: Initialize frequency map
        freq = {}
        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1

        x = 0
        y = 0

        # Step 2: Iterate through the frequency map and determine counts for x and y
        for char, count in freq.items():
            # Get the position of the character in the alphabet (1-based index)
            position = ord(char) - ord('a') + 1
            if position % 2 == 0:  # Even position in the alphabet
                if count % 2 == 0:  # Even frequency
                    x += 1
            else:  # Odd position in the alphabet
                if count % 2 != 0:  # Odd frequency
                    y += 1

        # Step 3: Determine if the sum of x and y is even or odd
        if (x + y) % 2 == 0:
            return "EVEN"
        else:
            return "ODD"