# https://leetcode.com/problems/count-zero-request-servers/

# Example 1:
# Input: n = 3, logs = [[1,3],[2,6],[1,5]], x = 5, queries = [10,11]
# Output: [1,2]
# Explanation: 
# For queries[0]: The servers with ids 1 and 2 get requests in the duration of [5, 10]. Hence, only server 3 gets zero requests.
# For queries[1]: Only the server with id 2 gets a request in duration of [6,11]. Hence, the servers with ids 1 and 3 are the only servers that do not receive any requests during that time period.

from typing import List

class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        # Initialise the log count for each server.
        dico = {i: 0 for i in range(1, n + 1)}

        # Sort logs by timestamp to process them using a sliding window.
        logs = sorted(logs, key=lambda x: x[1])

        # Sort queries by time while preserving their original indices.
        queries = sorted([query, i] for i, query in enumerate(queries))

        p = len(logs)

        # right points to the next log to include in the window.
        # left tracks the last log that has been removed from the window.
        right, left = 0, -1

        # Initially, all servers have zero logs in the observation window.
        countNull = n

        # Store answers in the original query order.
        res = [0] * len(queries)

        # Process queries in increasing order of timestamp.
        for query, i in queries:

            # Include all logs with timestamps <= query.
            while right < p and logs[right][1] <= query:
                serv = logs[right][0]

                # If this server had no logs, it is no longer inactive.
                if dico[serv] == 0:
                    countNull -= 1

                # Increment the server's log count.
                dico[serv] += 1
                right += 1

            # Remove logs with timestamps strictly less than query - x.
            # This keeps only logs within the interval [query - x, query].
            while left + 1 < p and logs[left + 1][1] < query - x:
                left += 1
                serv = logs[left][0]

                # Decrement the server's log count.
                dico[serv] -= 1

                # If its count becomes zero, the server is inactive again.
                if dico[serv] == 0:
                    countNull += 1

            # Store the number of servers with no logs in the current window.
            res[i] = countNull

        # Return answers in the original order of queries.
        return res
    