# https://leetcode.com/problems/binary-watch/

# Example 1:
# Input: turnedOn = 1
# Output: ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]

from typing import List

class Solution:
    def readBinaryWatch(self, k: int) -> List[str]:
        # If no LEDs are ON → only possible time
        if k == 0:
            return ['0:00']

        # Binary watch uses:
        # 4 bits for hour + 6 bits for minutes = 10 bits total

        # mask = 000000111111 (6 ones)
        # Used to extract minute bits (last 6 bits)
        mask = (1 << 6) - 1

        # Smallest number having exactly k bits set
        # Example: k=3 → 0000000111
        q = (1 << k) - 1

        # Largest configuration with k bits inside 10-bit space
        # shifts k ones to the leftmost valid position
        limit = q << (10 - k)

        res = []

        # Iterate over all numbers having exactly k bits set
        while q <= limit:

            # Extract minutes (lower 6 bits)
            min = q & mask

            # Extract hours (upper remaining bits)
            hour = q >> 6

            # Valid binary watch constraints
            # hours: 0–11
            # minutes: 0–59
            if hour < 12 and min < 60:
                # Format minutes with leading zero if needed
                res.append(f'{hour}:{min:0>2}')

            # ---- Next combination with same number of set bits ----
            # This is Gosper's Hack (bit manipulation trick)

            # Get rightmost set bit
            r = q & -q

            # Add it to create next higher pattern
            n = q + r

            # Rearrange remaining bits to maintain k set bits
            q = (((q ^ n) // r) >> 2) | n

        return res
