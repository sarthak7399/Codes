# https://leetcode.com/problems/string-compression/description/?envType=study-plan-v2&envId=leetcode-75&__cf_chl_tk=HyYodGpGHXln3lCBwgSgMz5Mt5F17V1WwKfbVKqTu9I-1706898763-0-gaNycGzNElA

# Example 1:
# Input: chars = ["a","a","b","b","c","c","c"]
# Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
# Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".

# Example 3:
# Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
# Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
# Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".

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
