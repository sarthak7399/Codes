# https://leetcode.com/problems/count-and-say/

# Example 1:
# Input: n = 4
# Output: "1211"
# Explanation:
# countAndSay(1) = "1"
# countAndSay(2) = RLE of "1" = "11"
# countAndSay(3) = RLE of "11" = "21"
# countAndSay(4) = RLE of "21" = "1211"

class Solution:
    def countAndSay(self, n: int) -> str:
        # Base case: The first term in the sequence is "1"
        if n == 1:
            return "1"
        # Recursively get the (n-1)th term and convert it to the nth term
        return self.converter(self.countAndSay(n - 1))

    def converter(self, num: str) -> str:
        i = 0  # Pointer to traverse the input string
        res = ""  # To store the result string

        # Loop through the input string
        while i < len(num):
            cnt = 1  # Initialize count of current digit

            # Count the number of consecutive same digits
            while i + 1 < len(num) and num[i] == num[i + 1]:
                cnt += 1
                i += 1

            # Append the count and digit to the result string
            res += str(cnt) + num[i]
            i += 1  # Move to the next new digit

        return res
