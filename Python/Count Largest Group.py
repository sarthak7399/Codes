# https://leetcode.com/problems/count-largest-group/

# Example 1:
# Input: n = 13
# Output: 4
# Explanation: There are 9 groups in total, they are grouped according sum of its digits of numbers from 1 to 13:
# [1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9].
# There are 4 groups with largest size.

class Solution:
    def countLargestGroup(self, n: int) -> int:
        num_str = str(n + 1)  # Convert n+1 to string for digit-wise processing
        max_digit_sum = len(num_str) * 9 + 1  # Max possible digit sum (all 9s)
        
        digit_sum_count = [0] * max_digit_sum  # DP array to count frequency of each digit sum
        digit_sum_so_far = 0  # Running sum of digits while traversing
        
        for ch in num_str:
            digit = int(ch)
            new_digit_sum_count = [0] * max_digit_sum
            
            # Expand all previously counted digit sums with digits 0–9
            for prev_sum in range(max_digit_sum):
                for d in range(10):
                    if prev_sum + d < max_digit_sum:
                        new_digit_sum_count[prev_sum + d] += digit_sum_count[prev_sum]
            
            digit_sum_count = new_digit_sum_count
            
            # Handle the current digit to add new combinations
            for d in range(digit):
                if digit_sum_so_far + d < max_digit_sum:
                    digit_sum_count[digit_sum_so_far + d] += 1

            digit_sum_so_far += digit
        
        digit_sum_count[0] = 0  # Remove count for digit sum 0 (not valid for positive integers)

        max_frequency = max(digit_sum_count)  # Find the maximum frequency
        return digit_sum_count.count(max_frequency)  # Count how many digit sums have this frequency
