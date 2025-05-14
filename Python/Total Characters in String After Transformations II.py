# https://leetcode.com/problems/total-characters-in-string-after-transformations-ii/

# Example 1:
# Input: s = "abcyy", t = 2, nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]
# Output: 7
# Explanation:
# First Transformation (t = 1):
# 'a' becomes 'b' as nums[0] == 1
# 'b' becomes 'c' as nums[1] == 1
# 'c' becomes 'd' as nums[2] == 1
# 'y' becomes 'z' as nums[24] == 1
# 'y' becomes 'z' as nums[24] == 1
# String after the first transformation: "bcdzz"
# Second Transformation (t = 2):
# 'b' becomes 'c' as nums[1] == 1
# 'c' becomes 'd' as nums[2] == 1
# 'd' becomes 'e' as nums[3] == 1
# 'z' becomes 'ab' as nums[25] == 2
# 'z' becomes 'ab' as nums[25] == 2
# String after the second transformation: "cdeabab"
# Final Length of the string: The string is "cdeabab", which has 7 characters.

from typing import List

class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        MOD = 10**9 + 7  # Use modulo to keep values within bounds for large inputs

        # Initialize the transformation matrix
        # transition[i][j] = how many times character i can transform into character j in 1 transformation step
        transition = [[0] * 26 for _ in range(26)]
        for c in range(26):  # For each character from 'a' to 'z'
            num = nums[c]    # The number of characters ahead it can transform into
            for j in range(1, num + 1):
                next_char = (c + j) % 26  # Wrap around using modulo
                transition[c][next_char] += 1  # One way to transform from c → next_char

        # Multiply two 26x26 matrices under modulo
        def multiply(a, b):
            res = [[0] * 26 for _ in range(26)]
            for i in range(26):
                for k in range(26):
                    if a[i][k] == 0:
                        continue  # Skip unnecessary multiplications
                    for j in range(26):
                        res[i][j] = (res[i][j] + a[i][k] * b[k][j]) % MOD
            return res

        # Perform fast exponentiation on the transition matrix
        def matrix_pow(mat, power):
            result = [[1 if i == j else 0 for j in range(26)] for i in range(26)]  # Identity matrix
            while power > 0:
                if power % 2 == 1:
                    result = multiply(result, mat)
                mat = multiply(mat, mat)
                power //= 2
            return result

        # Compute transition matrix raised to power t, representing t transformations
        mat_pow = matrix_pow(transition, t)

        # Initialize count vector from the string s
        # cnt[i] = how many times character 'a'+i appears in the string
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - ord('a')] += 1

        # Apply matrix transformation to the count vector
        new_cnt = [0] * 26
        for i in range(26):       # For each original character
            for j in range(26):   # Distribute its count across all possible results
                new_cnt[j] = (new_cnt[j] + cnt[i] * mat_pow[i][j]) % MOD

        # Sum all resulting counts to get the final length of the transformed string
        total = 0
        for x in new_cnt:
            total = (total + x) % MOD

        return total
