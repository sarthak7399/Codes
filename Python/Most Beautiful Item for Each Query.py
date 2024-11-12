# https://leetcode.com/problems/most-beautiful-item-for-each-query/

# Example 1:
# Input: items = [[1,2],[3,2],[2,4],[5,6],[3,5]], queries = [1,2,3,4,5,6]
# Output: [2,4,5,5,6,6]
# Explanation:
# - For queries[0]=1, [1,2] is the only item which has price <= 1. Hence, the answer for this query is 2.
# - For queries[1]=2, the items which can be considered are [1,2] and [2,4]. 
#   The maximum beauty among them is 4.
# - For queries[2]=3 and queries[3]=4, the items which can be considered are [1,2], [3,2], [2,4], and [3,5].
#   The maximum beauty among them is 5.
# - For queries[4]=5 and queries[5]=6, all items can be considered.
#   Hence, the answer for them is the maximum beauty of all items, i.e., 6.

class Solution(object):
    def maximumBeauty(self, items, queries):
        
        maxI = float('inf')  # Infinite value for marking upper bounds
        res = [[0, 0, maxI]]  # Initialize res with base entry [price, beauty, next_price_limit]

        # Sort items by price
        items.sort(key=lambda x: x[0])

        # Construct res list with significant price-beauty pairs
        for price, beauty in items:
            lastBracket = res[-1]  # Get the most recent price bracket
            if beauty > lastBracket[1]:  # Only add if beauty is an improvement
                res[-1][2] = price  # Set upper price limit for previous bracket
                res.append([price, beauty, maxI])  # Append new bracket with current price and beauty

        ans = []  # List to store results for each query

        # Process each query by searching backwards in res
        for x in queries:
            for i in range(len(res) - 1, -1, -1):  # Start from end for efficiency
                if res[i][0] <= x:  # Find the max beauty where price <= query price
                    ans.append(res[i][1])
                    break  # Move to the next query once a valid bracket is found

        return ans
