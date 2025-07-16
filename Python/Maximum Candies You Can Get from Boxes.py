# https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes/

# Example 1:
# Input: status = [1,0,1,0], candies = [7,5,4,100], keys = [[],[],[1],[]], containedBoxes = [[1,2],[3],[],[]], initialBoxes = [0]
# Output: 16
# Explanation: You will be initially given box 0. You will find 7 candies in it and boxes 1 and 2.
# Box 1 is closed and you do not have a key for it so you will open box 2. You will find 4 candies and a key to box 1 in box 2.
# In box 1, you will find 5 candies and box 3 but you will not find a key to box 3 so box 3 will remain closed.
# Total number of candies collected = 7 + 4 + 5 = 16 candy.

from collections import deque

class Solution:
    def maxCandies(self, stat, choco, keys, containedBoxes, curBoxes):
        dq = deque()  # Double-ended queue to process boxes in BFS-like order

        # Process initial boxes
        for box_ind in curBoxes:
            # If the box gives a key to another box, mark that box as now unlockable
            for key in keys[box_ind]:
                stat[key] = 1  # Mark box as unlocked (we now have the key)

            # If this box is not yet openable, add to the end (wait for key)
            if stat[box_ind] == 0:
                dq.append(box_ind)
            else:
                # If box is already openable, process it first
                dq.appendleft(box_ind)

        ans = 0  # Total number of candies collected

        while dq:
            ind = dq.popleft()

            # If the box is still locked (no key), skip processing
            if stat[ind] == 0:
                break

            # If box is openable
            elif stat[ind] == 1:
                ans += choco[ind]  # Collect candies in the box

                # Use all the keys found in this box to unlock others
                for key in keys[ind]:
                    stat[key] = 1  # Unlock box with the key

            # Add all contained boxes into the queue
            for new_box_ind in containedBoxes[ind]:
                if stat[new_box_ind] == 0:
                    dq.append(new_box_ind)       # Locked boxes go to the end
                else:
                    dq.appendleft(new_box_ind)   # Unlocked boxes go to the front

        return ans  # Return the total candies collected
