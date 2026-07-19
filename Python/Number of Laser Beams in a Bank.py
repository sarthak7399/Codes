# https://leetcode.com/problems/number-of-laser-beams-in-a-bank/

# Example 1:
# Input: bank = ["011001","000000","010100","001000"]
# Output: 8
# Explanation: Between each of the following device pairs, there is one beam. In total, there are 8 beams:
#  * bank[0][1] -- bank[2][1]
#  * bank[0][1] -- bank[2][3]
#  * bank[0][2] -- bank[2][1]
#  * bank[0][2] -- bank[2][3]
#  * bank[0][5] -- bank[2][1]
#  * bank[0][5] -- bank[2][3]
#  * bank[2][1] -- bank[3][2]
#  * bank[2][3] -- bank[3][2]
# Note that there is no beam between any device on the 0th row with any on the 3rd row.
# This is because the 2nd row contains security devices, which breaks the second condition.

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        """
        Calculates the total number of security beams between rows in a bank.
        Each string in 'bank' represents a row of devices ('1' = device, '0' = empty space).
        A beam exists between two rows only if both have at least one device.
        """

        interList = []  # To store the count of devices ('1's) in each non-empty row

        # Count number of '1's in each row and store only non-zero counts
        for element in bank:
            count = element.count('1')
            if count != 0:
                interList.append(count)

        beamCount = 0  # Total number of beams

        # If there's only one or zero rows with devices, no beams can exist
        if len(interList) <= 1:
            return beamCount

        # Multiply adjacent non-empty row device counts to get beams between them
        i = 0
        while i < len(interList) - 1:
            beamCount += interList[i] * interList[i + 1]
            i += 1

        return beamCount
