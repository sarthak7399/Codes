# https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/?envType=daily-question&envId=2024-03-05

# Example 2:
# Input: s = "cabaabac"
# Output: 0
# Explanation: An optimal sequence of operations is:
# - Take prefix = "c" and suffix = "c" and remove them, s = "abaaba".
# - Take prefix = "a" and suffix = "a" and remove them, s = "baab".
# - Take prefix = "b" and suffix = "b" and remove them, s = "aa".
# - Take prefix = "a" and suffix = "a" and remove them, s = "".

# Example 3:
# Input: s = "aabccabba"
# Output: 3
# Explanation: An optimal sequence of operations is:
# - Take prefix = "aa" and suffix = "a" and remove them, s = "bccabb".
# - Take prefix = "b" and suffix = "bb" and remove them, s = "cca".

class Solution:
  def minimumLength(self, s: str) -> int:
    i, j = 0, len(s) - 1  # Initialize the pointers at the beginning and end of the string
    while (i < j and s[i] == s[j]):  # Continue while the characters at the current positions are the same and the pointers haven't crossed each other
      while i < j and s[i] == s[i + 1]:  # Skip consecutive matching characters from the beginning of the string
        i += 1
      while i < j and s[j] == s[j - 1]:  # Skip consecutive matching characters from the end of the string
        j -= 1
      i += 1  # Move the pointer towards the center of the string
      j -= 1  # Move the pointer towards the center of the string
    return max(j - i + 1, 0)  # Return the length of the remaining substring, ensuring it's non-negative