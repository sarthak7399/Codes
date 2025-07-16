# https://leetcode.com/problems/sum-of-k-mirror-numbers/

# Example 1:
# Input: k = 2, n = 5
# Output: 25
# Explanation:
# The 5 smallest 2-mirror numbers and their representations in base-2 are listed as follows:
#   base-10    base-2
#     1          1
#     3          11
#     5          101
#     7          111
#     9          1001
# Their sum = 1 + 3 + 5 + 7 + 9 = 25. 

class Solution:
    def createPalindrome(self, num: int, odd: bool) -> int:
        """
        Constructs a palindrome from the given number `num`.
        If `odd` is True, the middle digit is not duplicated (odd-length palindrome).
        If `odd` is False, the entire number is mirrored (even-length palindrome).
        """
        x = num
        if odd:
            x //= 10  # Skip the middle digit for odd-length palindrome
        while x > 0:
            num = num * 10 + x % 10  # Append digits in reverse
            x //= 10
        return num

    def isPalindrome(self, num: int, base: int) -> bool:
        """
        Checks if the number `num` is a palindrome in base `base`.
        Converts the number into base `base` and checks if digits are symmetric.
        """
        digits = []
        while num > 0:
            digits.append(num % base)
            num //= base
        return digits == digits[::-1]  # Palindrome check

    def kMirror(self, k: int, n: int) -> int:
        """
        Returns the sum of the first `n` positive integers that are palindromic
        in both base 10 and base `k`.
        """
        total = 0       # Accumulates the total sum of k-mirror numbers
        length = 1      # Used to generate numbers of increasing length

        while n > 0:
            # Generate odd-length palindromes and check base-k palindrome condition
            for i in range(length, length * 10):
                if n <= 0:
                    break
                p = self.createPalindrome(i, True)
                if self.isPalindrome(p, k):
                    total += p
                    n -= 1

            # Generate even-length palindromes and check base-k palindrome condition
            for i in range(length, length * 10):
                if n <= 0:
                    break
                p = self.createPalindrome(i, False)
                if self.isPalindrome(p, k):
                    total += p
                    n -= 1

            length *= 10  # Increase the digit length for next iteration

        return total
