# https://leetcode.com/problems/calculate-digit-sum-of-a-string/

# Example 1:
# Input: s = "11111222223", k = 3
# Output: "135"
# Explanation: 
# - For the first round, we divide s into groups of size 3: "111", "112", "222", and "23".
#   ​​​​​Then we calculate the digit sum of each group: 1 + 1 + 1 = 3, 1 + 1 + 2 = 4, 2 + 2 + 2 = 6, and 2 + 3 = 5. 
#   So, s becomes "3" + "4" + "6" + "5" = "3465" after the first round.
# - For the second round, we divide s into "346" and "5".
#   Then we calculate the digit sum of each group: 3 + 4 + 6 = 13, 5 = 5. 
#   So, s becomes "13" + "5" = "135" after second round. 
# Now, s.length <= k, so we return "135" as the answer.

class Solution:
    def digitSum(self, s: str, k: int) -> str:
        # Continue grouping and summing digits until the string length is <= k
        while len(s) > k:
            next_s = ""

            # Process the string in chunks of size k
            for i in range(0, len(s), k):
                total = 0

                # Calculate the sum of digits in the current chunk
                for j in range(i, min(i + k, len(s))):
                    total += int(s[j])

                # Append the chunk's digit sum to the next string
                next_s += str(total)

            # Use the newly generated string for the next iteration
            s = next_s

        # Return the final string when its length is <= k
        return s