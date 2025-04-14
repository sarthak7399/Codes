# https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/

# Example 1:
# Input: limit = 4, queries = [[1,4],[2,5],[1,3],[3,4]]
# Output: [1,2,2,3]
# Explanation:
# After query 0, ball 1 has color 4.
# After query 1, ball 1 has color 4, and ball 2 has color 5.
# After query 2, ball 1 has color 3, and ball 2 has color 5.
# After query 3, ball 1 has color 3, ball 2 has color 5, and ball 3 has color 4.

from collections import defaultdict
class Solution(object):
    def queryResults(self, limit, queries):
        """
        :type limit: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        bal = {}  # Dictionary to store current balance for each key
        col = defaultdict(int)  # Default dictionary to count frequency of balances
        n = len(queries)  # Number of queries
        res = [0] * n  # Initialize result list with zeros

        for i in range(n):  # Iterate through each query
            key = queries[i][0]
            value = queries[i][1]

            if key not in bal:  # If key has no balance, set the initial balance
                bal[key] = value
            else:
                oldBalance = bal[key]
                if col[oldBalance] == 1:  # If old balance count is 1, remove it from col
                    del col[oldBalance]
                else:  # Decrease the frequency of the old balance
                    col[oldBalance] -= 1
                bal[key] = value  # Update balance for the key

            col[value] += 1  # Increase the count of the new balance
            res[i] = len(col)  # Set the result for this query as the number of distinct balances

        return res  # Return the result list
