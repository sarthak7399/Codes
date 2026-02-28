# https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/

# Example 3:
# Input: n = 12
# Output: 505379714
# Explanation: The concatenation results in "1101110010111011110001001101010111100".
# The decimal value of that is 118505380540.
# After modulo 109 + 7, the result is 505379714.

class Solution:
    def concatenatedBinary(self, n: int) -> int:
        # 'shifter' represents how many bits are needed
        # to represent the current number in binary.
        # Initially for number 1 → binary "1" → 1 bit
        shifter = 1
        
        # 'val' keeps track of the last power of 2 encountered.
        # Whenever we reach a new power of 2, number of bits increases.
        val = 1
        
        # This will store the final concatenated decimal value
        answer = 0
        
        # Modulo value to avoid integer overflow
        mod = 10**9 + 7
        
        # Iterate from 1 to n (inclusive)
        for a in range(1, n + 1):
            
            # If current number is a power of 2,
            # its binary length increases by 1.
            # Example:
            # 1 -> 1 bit
            # 2 -> 2 bits
            # 4 -> 3 bits
            # 8 -> 4 bits ...
            if val * 2 == a:
                shifter += 1   # increase bit length
                val = a        # update last power of 2
            
            # Left shift existing answer by 'shifter' bits
            # to make space for current number's binary digits,
            # then append 'a' using bitwise OR.
            #
            # Equivalent idea:
            # answer = binary_concat(answer, a)
            answer = ((answer << shifter) | a) % mod
            
        return answer