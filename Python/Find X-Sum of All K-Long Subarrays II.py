# https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-ii/

# Example 1:
# Input: nums = [1,1,2,2,3,4,2,3], k = 6, x = 2
# Output: [6,10,12]
# Explanation:
# For subarray [1, 1, 2, 2, 3, 4], only elements 1 and 2 will be kept in the resulting array. Hence, answer[0] = 1 + 1 + 2 + 2.
# For subarray [1, 2, 2, 3, 4, 2], only elements 2 and 4 will be kept in the resulting array. Hence, answer[1] = 2 + 2 + 2 + 4. Note that 4 is kept in the array since it is bigger than 3 and 1 which occur the same number of times.
# For subarray [2, 2, 3, 4, 2, 3], only elements 2 and 3 are kept in the resulting array. Hence, answer[2] = 2 + 2 + 2 + 3 + 3.

from typing import List
import heapq

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        """
        Compute the 'X-sum' for each sliding window of size k in the list 'nums'.
        The 'X-sum' is the sum of (value * frequency) for the top 'x' most frequent numbers
        in that window, breaking ties by larger number values.
        """

        n = len(nums)
        ans = [0] * (n - k + 1)   # Result list for each window

        cnt = {}                   # Stores current frequency of each number
        chosen = set()             # Stores top x elements currently contributing to total

        hot: list[tuple[int, int]] = []   # Min-heap of chosen elements (freq, value)
        pool: list[tuple[int, int]] = []  # Max-heap (via negation) of unchosen elements (-freq, -value)

        total = 0   # Current total X-sum for the window

        # 🔹 Remove outdated or invalid heap entries
        def clean():
            # Remove invalid entries from hot heap (chosen elements)
            while hot and (hot[0][1] not in chosen or cnt.get(hot[0][1], 0) != hot[0][0]):
                heapq.heappop(hot)

            # Remove invalid entries from pool heap (unchosen elements)
            while pool and ((-pool[0][1]) in chosen or cnt.get(-pool[0][1], 0) != -pool[0][0] or -pool[0][0] == 0):
                heapq.heappop(pool)

        # 🔹 If a value is currently chosen, remove its contribution
        def demote_if_chosen(v: int):
            nonlocal total
            if v in chosen:
                chosen.remove(v)
                total -= v * cnt.get(v, 0)

        # 🔹 Promote best candidates from pool to chosen, until we have x chosen elements
        def promote_if_needed():
            nonlocal total
            clean()
            while len(chosen) < x and pool:
                f, v = -pool[0][0], -pool[0][1]   # Get top from pool (max freq, max val)
                if cnt.get(v, 0) != f or v in chosen or f == 0:
                    heapq.heappop(pool)
                    continue
                heapq.heappop(pool)
                chosen.add(v)
                total += v * f
                heapq.heappush(hot, (f, v))
            clean()

        # 🔹 Add one instance of number `v` to the current window
        def add_one(v: int):
            nonlocal total
            demote_if_chosen(v)     # If it’s in chosen, temporarily demote (will re-evaluate)
            f = cnt.get(v, 0) + 1
            cnt[v] = f
            heapq.heappush(pool, (-f, -v))  # Add updated frequency to pool

            # Try promoting it if we have room or it's better than current chosen
            if len(chosen) < x:
                promote_if_needed()
            else:
                clean()
                if pool and hot:
                    bf, bv = -pool[0][0], -pool[0][1]  # Best candidate from pool
                    wf, wv = hot[0]                    # Worst chosen element
                    # If pool element has higher freq/value, replace worst chosen
                    if bf > wf or (bf == wf and bv > wv):
                        heapq.heappop(pool)
                        chosen.add(bv)
                        total += bv * bf
                        heapq.heappush(hot, (bf, bv))

                        heapq.heappop(hot)
                        if wv in chosen:
                            chosen.remove(wv)
                            total -= wv * wf
                        heapq.heappush(pool, (-wf, -wv))
                clean()

        # 🔹 Remove one instance of number `v` from current window
        def remove_one(v: int):
            nonlocal total
            demote_if_chosen(v)
            f = cnt.get(v, 0) - 1
            if f <= 0:
                cnt.pop(v, None)
            else:
                cnt[v] = f
                heapq.heappush(pool, (-f, -v))
            promote_if_needed()

        # 🔹 Initialize first window
        for i in range(k):
            add_one(nums[i])
        ans[0] = total

        # 🔹 Slide window through the array
        for i in range(k, n):
            remove_one(nums[i - k])  # remove leftmost
            add_one(nums[i])         # add new rightmost
            ans[i - k + 1] = total

        # 🔹 Return list of all window results
        return ans
