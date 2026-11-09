# https://leetcode.com/problems/find-servers-that-handled-most-number-of-requests/

# Example 1:
# Input: k = 3, arrival = [1,2,3,4,5], load = [5,2,3,3,3] 
# Output: [1] 
# Explanation: 
# All of the servers start out available.
# The first 3 requests are handled by the first 3 servers in order.
# Request 3 comes in. Server 0 is busy, so it's assigned to the next available server, which is 1.
# Request 4 comes in. It cannot be handled since all servers are busy, so it is dropped.
# Servers 0 and 2 handled one request each, while server 1 handled two requests. Hence server 1 is the busiest server.


from heapq import heappop, heappush
from statistics import multimode

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        # Initialise a min-heap of free servers.
        # Each server is represented by its next eligible request index.
        free = list(range(k))

        # handled stores the servers that successfully handled requests.
        # busy stores (time_when_server_becomes_free, server_index).
        handled, busy = [], []

        # Process each request along with its arrival time and processing load.
        for i, (t, d) in enumerate(zip(arrival, load)):

            # Release all servers whose requests are completed by time t.
            while busy and busy[0][0] <= t:
                # Calculate the server's next eligible request index.
                # The modulo operation determines its first turn at or after i.
                heappush(free, i + (heappop(busy)[1] - i) % k)

            # If no server is free, drop the current request.
            if free:
                # Select the server whose next eligible request index is smallest.
                # Modulo k converts that value back to the actual server index.
                x = heappop(free) % k

                # Mark the server as busy until the current request is completed.
                heappush(busy, (t + d, x))

                # Record the server that handled this request.
                handled.append(x)

        # Return the server(s) that handled the maximum number of requests.
        return multimode(handled)