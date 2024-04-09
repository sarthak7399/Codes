# https://leetcode.com/problems/time-needed-to-buy-tickets/

# Example 1:
# Input: tickets = [2,3,2], k = 2
# Output: 6
# Explanation: 
# - In the first pass, everyone in the line buys a ticket and the line becomes [1, 2, 1].
# - In the second pass, everyone in the line buys a ticket and the line becomes [0, 1, 0].
# The person at position 2 has successfully bought 2 tickets and it took 3 + 3 = 6 seconds.

from typing import List
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        count=0
        i=0
        while tickets[k]:
            if tickets[k]==0:break
            if tickets[i]>0:
                temp=tickets.pop(0)
                print(temp)
                temp-=1
                tickets=tickets+[temp]
                count+=1
            elif tickets[i]==0:
                tickets.pop(i)
            k = (k - 1) % (len(tickets))
            # print(tickets, count, k)
        return count