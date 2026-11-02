# https://leetcode.com/problems/count-commas-in-range-ii/

# Example 1:
# Input: n = 1002
# Output: 3
# Explanation:
# The numbers "1,000", "1,001", and "1,002" each contain one comma, giving a total of 3.

class Solution:
    def countCommas(self, n):
        # Numbers from 1 to 999 do not contain any commas.
        if n <= 999:
            return 0

        # Store the total number of commas used.
        totalCommas = 0

        # The first range containing commas is 1,000 to 999,999.
        rangeStart = 1000
        rangeEnd = rangeStart * 1000 - 1

        # Numbers in the current range contain this many commas.
        commas = 1

        # Process each range until we exceed n.
        while rangeStart <= n:
            # Count how many numbers from the current range are
            # present between rangeStart and n.
            numbers = min(n, rangeEnd) - rangeStart + 1

            # Add the total commas contributed by this range.
            totalCommas += commas * numbers

            # Stop if the current range already includes n.
            if rangeEnd > n:
                break

            # Move to the next comma range.
            # Example:
            # 1,000 -> 1 comma
            # 1,000,000 -> 2 commas
            # 1,000,000,000 -> 3 commas
            rangeStart *= 1000
            rangeEnd = rangeStart * 1000 - 1

            # Numbers in the next range contain one additional comma.
            commas += 1

        # Return the total number of commas used from 1 to n.
        return totalCommas