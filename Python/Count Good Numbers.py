# https://leetcode.com/problems/count-good-numbers/

# Example 1:
# Input: n = 1
# Output: 5
# Explanation: The good numbers of length 1 are "0", "2", "4", "6", "8".

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        Mod = 10**9 + 7  # Large prime for modulo to avoid overflow

        # Function to perform modular exponentiation: (x^exp) % Mod
        def powMod(x, exp):
            if exp == 0:
                return 1  # Base case: x^0 = 1
            y = x if (exp & 1) == 1 else 1  # If exp is odd, take x once
            # Recurse on x^2 with half exponent, combine with y
            return y * powMod((x * x) % Mod, exp >> 1) % Mod

        # Even positions (0-indexed): 0, 2, 4, ... → total (n+1)//2 digits
        n0 = (n + 1) // 2
        # Odd positions: 1, 3, 5, ... → remaining digits
        n1 = n - n0

        # For even indices, 5 options (0,2,4,6,8); for odd indices, 4 options (1,3,5,7,9)
        # Multiply combinations at even and odd places and take modulo
        return powMod(5, n0) * powMod(4, n1) % Mod
