# https://leetcode.com/problems/sum-game/

# Example 3:
# Input: num = "?3295???"
# Output: false
# Explanation: It can be proven that Bob will always win. One possible outcome is:
# - Alice replaces the first '?' with '9'. num = "93295???".
# - Bob replaces one of the '?' in the right half with '9'. num = "932959??".
# - Alice replaces one of the '?' in the right half with '2'. num = "9329592?".
# - Bob replaces the last '?' in the right half with '7'. num = "93295927".
# Bob wins because 9 + 3 + 2 + 9 = 5 + 9 + 2 + 7.

class Solution:
    def sumGame(self, num: str) -> bool:
        # Split the string into two equal halves.
        n = len(num)
        half = n // 2

        # sum1, sum2 store the known digit sums of both halves.
        # cnt1, cnt2 store the number of '?' characters in each half.
        sum1 = sum2 = cnt1 = cnt2 = 0

        # Process the left half.
        for c in num[:half]:
            if c == '?':
                cnt1 += 1
            else:
                sum1 += int(c)

        # Process the right half.
        for c in num[half:]:
            if c == '?':
                cnt2 += 1
            else:
                sum2 += int(c)

        # Count the total number of unknown digits.
        totalQ = cnt1 + cnt2

        # If the number of '?' is odd, Alice gets an unavoidable
        # advantage because she gets one more move than Bob.
        if totalQ % 2 == 1:
            return True

        # For an even number of '?', Bob can make both halves equal
        # only when the following balance condition is satisfied.
        #
        # If it is not satisfied, Alice can force the sums to differ.
        return 2 * (sum1 - sum2) != 9 * (cnt2 - cnt1)