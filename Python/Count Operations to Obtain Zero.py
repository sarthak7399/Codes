# https://leetcode.com/problems/count-operations-to-obtain-zero/

# Example 1:
# Input: num1 = 2, num2 = 3
# Output: 3
# Explanation: 
# - Operation 1: num1 = 2, num2 = 3. Since num1 < num2, we subtract num1 from num2 and get num1 = 2, num2 = 3 - 2 = 1.
# - Operation 2: num1 = 2, num2 = 1. Since num1 > num2, we subtract num2 from num1.
# - Operation 3: num1 = 1, num2 = 1. Since num1 == num2, we subtract num2 from num1.
# Now num1 = 0 and num2 = 1. Since num1 == 0, we do not need to perform any further operations.
# So the total number of operations required is 3.

class Solution:
    def countOperations(self, n1: int, n2: int) -> int:
        c = 0  # operation counter
        while n1 and n2:
            c += n1 // n2  # count how many times n2 fits into n1
            n1 %= n2       # reduce n1 by modulo
            n1, n2 = n2, n1  # swap for next iteration
        return c  # total operations
