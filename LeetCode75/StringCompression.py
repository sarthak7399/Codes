from typing import List
class Solution:
    def compress(self, chars: List[str]) -> int:
        count, index = 1, 0
        if len(chars) == 1: return 1        
        for current_index in range(1, len(chars) + 1):    # Iterate through the characters starting from the second one
            if current_index < len(chars) and chars[current_index] == chars[current_index - 1]: count += 1    # If the current character is the same as the previous one, increment the count
            else:
                chars[index] = chars[current_index - 1]     # Write the previous character at the current index
                index += 1
                if count > 1:       # If the count is greater than 1, write the count as a digit
                    for digit in str(count):
                        chars[index] = digit
                        index += 1
                count = 1
        return index
