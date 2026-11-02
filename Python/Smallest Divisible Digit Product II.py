# https://leetcode.com/problems/smallest-divisible-digit-product-ii/

# Example 1:
# Input: num = "1234", t = 256
# Output: "1488"
# Explanation:
# The smallest zero-free number that is greater than 1234 and has the product of its digits divisible by 256 is 1488, with the product of its digits equal to 256.

from math import gcd

class Solution:
    def smallestNumber(self, num: str, t: int) -> str:

        # Build the smallest possible suffix of the given size
        # whose digit product is divisible by req.
        def build_end(req, size):
            res = []

            # Factor req using digits 9 down to 2.
            # Using larger digits first helps minimise the number
            # of digits required.
            for f in range(9, 1, -1):
                while req % f == 0:
                    req //= f
                    res.append(str(f))

            # Fill unused positions with 1s, which do not
            # affect the product.
            if len(res) < size:
                res += ['1'] * (size - len(res))

            # Reverse to obtain the smallest lexicographical suffix.
            return "".join(res[::-1])

        # Length of the original number
        n = len(num)

        # Check whether t can be represented using decimal digits.
        # Every digit from 1 to 9 only contains prime factors
        # 2, 3, 5, and 7.
        curr = t

        for f in [2, 3, 5, 7]:
            while curr % f == 0:
                curr //= f

        # If another prime factor remains, no valid number exists.
        if curr != 1:
            return '-1'

        # rem[i] stores the remaining factor of t after processing
        # the first i digits of num.
        rem = [0] * (n + 1)
        rem[0] = t

        for i in range(n):

            # A zero makes the digit product zero, so stop processing
            # the original number beyond the first zero.
            if num[i] == '0':
                break

            # Remove the factors contributed by the current digit.
            rem[i + 1] = rem[i] // gcd(rem[i], int(num[i]))

        # If all required factors have already been satisfied,
        # num itself is the answer.
        if rem[-1] == 1:
            return num

        # Find the first zero, since positions after it cannot be
        # used while keeping the number prefix valid.
        z = num.find('0')
        start = z if z != -1 else n - 1

        # Try changing a digit from right to left.
        # This keeps the resulting number as small as possible.
        for i in range(start, -1, -1):

            # Number of positions available after the changed digit.
            end_size = n - i - 1

            # Try the smallest digit that is greater than num[i].
            for d in range(int(num[i]) + 1, 10):

                # Calculate the remaining requirement after choosing d.
                last = build_end(
                    rem[i] // gcd(rem[i], d),
                    end_size
                )

                # If the suffix fits within the required length,
                # we have found the smallest valid number.
                if len(last) == end_size:
                    return num[:i] + str(d) + last

        # If no number of the same length works, construct the
        # smallest valid number with n + 1 digits.
        return build_end(t, n + 1)