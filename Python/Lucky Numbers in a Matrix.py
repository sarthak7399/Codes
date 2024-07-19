# https://leetcode.com/problems/lucky-numbers-in-a-matrix/

# Example 1:
# Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
# Output: [15]
# Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column.

class Solution:
    def luckyNumbers(self, matrix):
        N = len(matrix)
        M = len(matrix[0])

        rowMin = []
        for i in range(N):
            rMin = float('inf')
            for j in range(M):
                rMin = min(rMin, matrix[i][j])
            rowMin.append(rMin)

        colMax = []
        for i in range(M):
            cMax = float('-inf')
            for j in range(N):
                cMax = max(cMax, matrix[j][i])
            colMax.append(cMax)

        luckyNumbers = []
        for i in range(N):
            for j in range(M):
                if matrix[i][j] == rowMin[i] and matrix[i][j] == colMax[j]:
                    luckyNumbers.append(matrix[i][j])

        return luckyNumbers
        