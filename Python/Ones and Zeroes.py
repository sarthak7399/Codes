# https://leetcode.com/problems/ones-and-zeroes/

# Example 1:
# Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
# Output: 4
# Explanation: The largest subset with at most 5 0's and 3 1's is {"10", "0001", "1", "0"}, so the answer is 4.
# Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}.
# {"111001"} is an invalid subset because it contains 4 1's, greater than the maximum of 3.

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = {(0, 0): 0}  # DP dictionary: (zeroes, ones) → max subset size

        for s in strs:
            ones = s.count('1')
            zeroes = s.count('0')
            newdp = {}  # temporary updates for current string

            for (prevZeroes, prevOnes), val in dp.items():
                newZeroes, newOnes = prevZeroes + zeroes, prevOnes + ones
                # check if within limits and improves result
                if newZeroes <= m and newOnes <= n:
                    if (newZeroes, newOnes) not in dp or dp[(newZeroes, newOnes)] < val + 1:
                        newdp[(newZeroes, newOnes)] = val + 1

            dp.update(newdp)  # merge updates

        return max(dp.values())  # return max subset size
