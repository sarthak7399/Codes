# https://leetcode.com/problems/count-symmetric-integers/

# Example 1:
# Input: low = 1, high = 100
# Output: 9
# Explanation: There are 9 symmetric integers between 1 and 100: 11, 22, 33, 44, 55, 66, 77, 88, and 99.

class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0  # Initialize a counter to track symmetric integers

        # Iterate over all numbers in the given range
        for num in range(low, high + 1):
            s = str(num)  # Convert the number to a string for easy digit access

            # Only consider numbers with even number of digits
            if len(s) % 2 == 0:
                mid = len(s) // 2  # Find the midpoint of the digit string

                # Calculate the sum of digits in the first and second halves
                left_sum = sum(map(int, s[:mid]))
                right_sum = sum(map(int, s[mid:]))

                # If both halves have equal digit sums, it's symmetric
                if left_sum == right_sum:
                    count += 1

        return count  # Return the total number of symmetric integers found
