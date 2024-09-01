# https://leetcode.com/problems/palindrome-partitioning/

# Example 1:
# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]

from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(substring):
            return substring == substring[::-1]

        def backtrack(start_idx, current_partition):
            # If we have reached the end of the string, add the current partition to the result
            if start_idx == len(s):
                result.append(current_partition[:])
                return
            
            # Try all possible substrings starting from the current index
            for end_idx in range(start_idx + 1, len(s) + 1):
                # Check if the current substring is a palindrome
                if is_palindrome(s[start_idx:end_idx]):
                    # If it is a palindrome, recursively find partitions for the remaining string
                    backtrack(end_idx, current_partition + [s[start_idx:end_idx]])

        result = []
        # Start backtrack from the beginning of the string with an empty partition
        backtrack(0, [])
        return result
