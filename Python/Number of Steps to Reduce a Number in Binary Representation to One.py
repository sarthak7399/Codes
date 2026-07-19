# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/

# Example 1:
# Input: s = "1101"
# Output: 6
# Explanation: "1101" corressponds to number 13 in their decimal representation.
# Step 1) 13 is odd, add 1 and obtain 14. 
# Step 2) 14 is even, divide by 2 and obtain 7.
# Step 3) 7 is odd, add 1 and obtain 8.
# Step 4) 8 is even, divide by 2 and obtain 4.  
# Step 5) 4 is even, divide by 2 and obtain 2. 
# Step 6) 2 is even, divide by 2 and obtain 1.  

class Solution:
    def numSteps(self, s: str) -> int:
        # Convert binary string to integer
        # Example: "1101" -> 13
        num = int(s, 2)

        # (Debug print — not needed for final solution)
        print(num)

        # Count number of operations required
        count = 0

        # Repeat operations until number becomes 1
        while True:
            # Stop condition
            if num == 1:
                break

            # If number is even → divide by 2
            # (right shift in binary)
            if num % 2 == 0:
                num //= 2
            else:
                # If number is odd → add 1
                # This creates carry in binary
                num += 1

            # One operation completed
            count += 1

        return count