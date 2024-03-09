# https://leetcode.com/problems/count-elements-with-maximum-frequency/?envType=daily-question&envId=2024-03-08

# Example 1:
# Input: nums = [1,2,2,3,1,4]
# Output: 4
# Explanation: The elements 1 and 2 have a frequency of 2 which is the maximum frequency in the array.
# So the number of elements in the array with maximum frequency is 4.

from collections import Counter
class Solution(object):
    def maxFrequencyElements(self, nums):
        freq_counter = Counter(nums)            # Step 1: Count the frequencies of each element using Counter       
        max_frequency = max(freq_counter.values())          # Step 2: Find the maximum frequency among all elements
        max_freq_elements = [num for num, freq in freq_counter.items() if freq == max_frequency]            # Step 3: Find the elements with the maximum frequency
        total_frequency = max_frequency * len(max_freq_elements)            # Step 4: Calculate the total frequency by multiplying the maximum frequency by the number of elements with that frequency
        return total_frequency
