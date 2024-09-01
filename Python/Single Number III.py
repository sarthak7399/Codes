# https://leetcode.com/problems/single-number-iii/

# Example 1:
# Input: nums = [1,2,1,3,2,5]
# Output: [3,5]
# Explanation:  [5, 3] is also a valid answer.

class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        # Create a dictionary to count the occurrences of each number
        frequency_count = {}
        
        # Iterate through the list and update the count for each number
        for num in nums:
            if num in frequency_count:
                frequency_count[num] += 1
            else:
                frequency_count[num] = 1
        
        # Create a list to store numbers that appear exactly once
        unique_numbers = []
        
        # Iterate through the dictionary to find numbers with a count of one
        for num, count in frequency_count.items():
            if count == 1:
                unique_numbers.append(num)
        
        return unique_numbers
