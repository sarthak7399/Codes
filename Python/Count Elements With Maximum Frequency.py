# https://leetcode.com/problems/count-elements-with-maximum-frequency/

# Example 1:
# Input: nums = [1,2,2,3,1,4]
# Output: 4
# Explanation: The elements 1 and 2 have a frequency of 2 which is the maximum frequency in the array.
# So the number of elements in the array with maximum frequency is 4.

class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        # Frequency array for numbers in range [1..100] (constraint-based optimization)
        freq = [0] * 101  

        mx = 0   # stores the maximum frequency seen so far
        res = 0  # stores the sum of frequencies of elements with max frequency

        for n in nums:
            freq[n] += 1          # increase frequency of current number
            f = freq[n]           # get updated frequency

            if f > mx:            # found a new higher frequency
                mx = f            # update max frequency
                res = f           # reset result to this frequency (only this element so far)
            elif f == mx:         # if this element's frequency equals current max
                res += f          # add its frequency to result

        return res  # return total count of elements with maximum frequency
