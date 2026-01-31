# https://leetcode.com/problems/find-smallest-letter-greater-than-target/

# Example 3:
# Input: letters = ["x","x","y","y"], target = "z"
# Output: "x"
# Explanation: There are no characters in letters that is lexicographically greater than 'z' so we return letters[0].

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # Default answer is the first letter (handles wrap-around case)
        res = letters[0]

        # Flag to mark when we have found at least one valid letter > target
        flag = False

        # Traverse all letters
        for ch in letters:
            if not flag:
                # First time we find a letter greater than target
                if ch > target:
                    res = ch
                    flag = True
            else:
                # If already found one, try to find a smaller valid candidate
                if ch > target and ch < res:
                    res = ch

        return res
