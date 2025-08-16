# https://leetcode.com/problems/maximum-69-number/

# Example 1:
# Input: num = 9669
# Output: 9969
# Explanation: 
# Changing the first digit results in 6669.
# Changing the second digit results in 9969.
# Changing the third digit results in 9699.
# Changing the fourth digit results in 9666.
# The maximum number is 9969.

class Solution:
    def maximum69Number(self, num: int) -> int:
        # Start checking digits from the thousands place (since num ≤ 9999 as per constraints)
        i = 1000

        # Traverse each digit from left (most significant) to right (least significant)
        while i > 0:
            # Extract the digit at current place by dividing and modding
            if (num // i) % 10 == 6:
                # If the digit is '6', change it to '9'
                # Adding 3*i works because:
                #   - At place value 'i', digit 6 → 9 is an increase by 3
                #   - So we add (3 * i) to the number to flip that digit
                num += 3 * i
                break  # Only flip the first '6' from left to maximize number
            i //= 10  # Move to the next digit place (divide by 10)

        # Return the updated number (maximum possible)
        return num
