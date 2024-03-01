# https://leetcode.com/problems/maximum-odd-binary-number/description/?envType=daily-question&envId=2024-03-01

# Example 1:
# Input: s = "010"
# Output: "001"
# Explanation: Because there is just one '1', it must be in the last position. So the answer is "001".

# Example 2:
# Input: s = "0101"
# Output: "1001"
# Explanation: One of the '1's must be in the last position. The maximum number that can be made with the remaining digits is "100". So the answer is "1001".

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones_count = s.count("1")       # Count the number of "1"s in the string
        zeros_count = len(s) - ones_count       # Calculate the number of "0"s in the string
        return "1" * (ones_count - 1) + "0" * zeros_count + "1"     # Return a binary string where all "1"s except the last one are preserved, followed by "0"s, and ending with "1"
        
