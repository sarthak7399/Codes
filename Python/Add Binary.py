# https://leetcode.com/problems/add-binary/

# Example 1:
# Input: a = "11", b = "1"
# Output: "100"

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        # Start from the last index (LSB - Least Significant Bit)
        i = len(a) - 1
        j = len(b) - 1
        
        carry = 0            # stores carry generated during addition
        result = []          # stores result bits (in reverse order)
        
        # Continue while digits remain OR carry exists
        while i >= 0 or j >= 0 or carry:
            total = carry    # start with previous carry
            
            # Add bit from string 'a' if available
            if i >= 0:
                total += int(a[i])
                i -= 1
            
            # Add bit from string 'b' if available
            if j >= 0:
                total += int(b[j])
                j -= 1
            
            # Current bit = remainder when divided by 2
            result.append(str(total % 2))
            
            # Carry = division by 2
            carry = total // 2
        
        # Reverse result because we built it from right → left
        return "".join(result[::-1])
