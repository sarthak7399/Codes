# https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/

# Example 1:
# Input: nums = [18,43,36,13,7]
# Output: 54
# Explanation: The pairs (i, j) that satisfy the conditions are:
# - (0, 2), both numbers have a sum of digits equal to 9, and their sum is 18 + 36 = 54.
# - (1, 4), both numbers have a sum of digits equal to 7, and their sum is 43 + 7 = 50.
# So the maximum sum that we can obtain is 54.

from collections import defaultdict
from typing import List
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        # We can group on dictionary, where key is sum of the digits of each num[i]
        # and value is the array containing all the nums[j] that have the same sum of digits
        # Later on iterate over arrays and get max value.
        
        # Define an inner function
        def sum_num_digits(num: int)->int:
            digit_sum = 0
            while num:
                digit_sum += num % 10
                num //= 10
            return digit_sum

        num_grouping = defaultdict(list)
        for num in nums:
            digits_sum = sum_num_digits(num)
            num_grouping[digits_sum].append(num)
        answer = -1
        for values in num_grouping.values():
            if len(values) > 1:
                values.sort(reverse=True)
                # We need the biggest sum of num[i] + num[j] so sort in descending order
                answer = max(answer, values[0]+values[1])
        return answer    

            
        