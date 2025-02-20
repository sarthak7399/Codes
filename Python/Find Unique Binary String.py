# https://leetcode.com/problems/find-unique-binary-string/

# Example 1:
# Input: nums = ["01","10"]
# Output: "11"
# Explanation: "11" does not appear in nums. "00" would also be correct.

class Solution:
    def findDifferentBinaryString(self, nums):
        result = []  # Initialize an empty list to store the result
        for i in range(len(nums)):  # Iterate over each index in the list
            if nums[i][i] == '0':  # Check the character at the diagonal position
                result.append('1')  # Append '1' if it's '0'
            else:
                result.append('0')  # Append '0' if it's '1'
        return ''.join(result)  # Join the list into a string and return it
