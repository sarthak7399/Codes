# https://leetcode.com/problems/plus-one/

# Example 1:
# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Traverse digits from right to left
        for i in range(len(digits) - 1, -1, -1):
            # If current digit is less than 9, just add 1 and return
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # If digit is 9, it becomes 0 and carry continues
            digits[i] = 0

        # If all digits were 9, add a leading 1
        return [1] + digits
