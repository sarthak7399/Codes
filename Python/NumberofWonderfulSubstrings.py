# https://leetcode.com/problems/number-of-wonderful-substrings/

# Example 1:
# Input: word = "aba"
# Output: 4
# Explanation: The four wonderful substrings are underlined below:
# - "aba" -> "a"
# - "aba" -> "b"
# - "aba" -> "a"
# - "aba" -> "aba"

class Solution:
    def wonderfulSubstrings(self, word):
        # Initialize an array to store the count of XOR values
        xor_count = [0] * 1024  # 2^10 to store XOR values
        # Initialize the result variable to store the count of wonderful substrings
        result = 0
        # Initialize the prefix XOR value
        prefix_xor = 0
        # Set the count of prefix XOR value 0 to 1
        xor_count[prefix_xor] = 1
        
        # Iterate through each character in the word
        for char in word:
            # Calculate the index of the character in the alphabet
            char_index = ord(char) - ord('a')
            # Update the prefix XOR value by XORing with the current character
            prefix_xor ^= 1 << char_index
            # Update the result by adding the count of the current prefix XOR value
            result += xor_count[prefix_xor]
            # Iterate through each bit position (0-9)
            for i in range(10):
                # Update the result by adding the count of substrings with different bit at i-th position
                result += xor_count[prefix_xor ^ (1 << i)]
            # Increment the count of the current prefix XOR value
            xor_count[prefix_xor] += 1
        
        return result
