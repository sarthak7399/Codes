# https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/

# Example 1:
# Input: s = "00110110", k = 2
# Output: true
# Explanation: The binary codes of length 2 are "00", "01", "10" and "11". They can be all found as substrings at indices 0, 1, 3 and 2 respectively.

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        req = 1 << k          # total number of binary codes of length k (2^k)
        seen = [False] * req  # tracks which k-length codes are seen
        mask = req - 1        # keeps only last k bits (bitmask like 111...k times)
        h = 0                 # rolling hash (integer form of last k bits)

        # Traverse string characters
        for i, ch in enumerate(s):
            # Shift left to make space for new bit,
            # apply mask to keep only last k bits,
            # add current bit (0 or 1)
            h = ((h << 1) & mask) | (ord(ch) & 1)

            # Start checking only after forming first k-length window
            if i >= k - 1 and not seen[h]:
                seen[h] = True   # mark this binary code as found
                req -= 1         # one required code satisfied

                # If all codes are found, return early
                if req == 0:
                    return True

        # Not all k-length binary codes appeared
        return False