# https://leetcode.com/problems/implement-router/

# Example 1:
# Input:
# ["Router", "addPacket", "addPacket", "addPacket", "addPacket", "addPacket", "forwardPacket", "addPacket", "getCount"]
# [[3], [1, 4, 90], [2, 5, 90], [1, 4, 90], [3, 5, 95], [4, 5, 105], [], [5, 2, 110], [5, 100, 110]]
# Output:
# [null, true, true, false, true, true, [2, 5, 90], true, 1]
# Explanation
# Router router = new Router(3); // Initialize Router with memoryLimit of 3.
# router.addPacket(1, 4, 90); // Packet is added. Return True.
# router.addPacket(2, 5, 90); // Packet is added. Return True.
# router.addPacket(1, 4, 90); // This is a duplicate packet. Return False.
# router.addPacket(3, 5, 95); // Packet is added. Return True
# router.addPacket(4, 5, 105); // Packet is added, [1, 4, 90] is removed as number of packets exceeds memoryLimit. Return True.
# router.forwardPacket(); // Return [2, 5, 90] and remove it from router.
# router.addPacket(5, 2, 110); // Packet is added. Return True.
# router.getCount(5, 100, 110); // The only packet with destination 5 and timestamp in the inclusive range [100, 110] is [4, 5, 105]. Return 1.

from collections import deque, defaultdict
import bisect

class Router(object):
    def __init__(self, memoryLimit):
        # Queue to maintain order of packets (FIFO eviction policy)
        self.q = deque()

        # Maximum memory capacity (number of packets the router can hold)
        self.m = memoryLimit

        # Set to keep track of all currently stored packets for quick lookup
        self.used_pac = set()

        # Current number of packets in memory
        self.l = 0

        # Mapping: destination -> sorted list of timestamps of packets
        # Helps in fast range queries with bisect
        self.dest_map = defaultdict(list)

    def addPacket(self, s, d, t):
        """
        Add a new packet to the router.
        s = source
        d = destination
        t = timestamp
        Returns True if packet added successfully, False if duplicate.
        """
        temp_p = (s, d, t)

        # Reject duplicate packet
        if temp_p in self.used_pac:
            return False

        # If memory full → remove the oldest packet
        if self.l >= self.m:
            old = self.q.popleft()            # remove from queue
            self.used_pac.remove(old)         # remove from set
            self.dest_map[old[1]].pop(0)      # remove earliest timestamp for that destination
            self.l -= 1                       # reduce count

        # Add new packet to structures
        self.q.append(temp_p)                 # queue
        self.used_pac.add(temp_p)             # set
        self.dest_map[d].append(t)            # store timestamp for destination
        self.l += 1                           # increase count

        return True

    def forwardPacket(self):
        """
        Forward the oldest packet (remove from router and return it).
        Returns [] if no packets available.
        """
        if self.l == 0:
            return []

        self.l -= 1
        p = self.q.popleft()                  # get oldest packet
        self.used_pac.remove(p)               # remove from set
        self.dest_map[p[1]].pop(0)            # remove timestamp for destination

        return list(p)                        # return packet as list [s, d, t]

    def getCount(self, d, s, e):
        """
        Get number of packets for destination 'd'
        with timestamps between [s, e] inclusive.
        Uses bisect for efficient range search.
        """
        a = self.dest_map[d]
        # Count = right index of e - left index of s
        return bisect.bisect_right(a, e) - bisect.bisect_left(a, s)
