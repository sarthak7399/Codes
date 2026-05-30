# https://leetcode.com/problems/block-placement-queries/

# Example 1:
# Input: queries = [[1,2],[2,3,3],[2,3,1],[2,2,2]]
# Output: [false,true,true]
# Explanation:
# For query 0, place an obstacle at x = 2. A block of size at most 2 can be placed before x = 3.

from typing import List

class Fenwick:
    def __init__(self, n: int) -> None:
        # Fenwick Tree (Binary Indexed Tree)
        # Used to maintain occupied positions and perform:
        # 1. Prefix sum queries
        # 2. K-th occupied position lookup
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, idx: int, val: int) -> None:
        # Add 'val' at position idx
        while idx <= self.n:
            self.bit[idx] += val
            idx += idx & -idx

    def sum(self, idx: int) -> int:
        # Returns prefix sum from 1 to idx
        res = 0
        while idx > 0:
            res += self.bit[idx]
            idx -= idx & -idx
        return res

    def kth(self, k: int) -> int:
        # Finds the smallest index whose prefix sum >= k
        idx = 0

        # Largest power of 2 <= n
        step = 1
        while (step << 1) <= self.n:
            step <<= 1

        d = step
        while d:
            nxt = idx + d

            if nxt <= self.n and self.bit[nxt] < k:
                idx = nxt
                k -= self.bit[nxt]

            d >>= 1

        return idx + 1


class SegTree:
    def __init__(self, n: int) -> None:
        # Segment Tree storing maximum gap lengths
        self.n = n
        self.tree = [0] * max(4, 4 * n)

    def update(self, node: int, l: int, r: int, pos: int, val: int) -> None:
        # Point update: set position 'pos' to value 'val'
        if l == r:
            self.tree[node] = val
            return

        mid = (l + r) // 2

        if pos <= mid:
            self.update(node * 2, l, mid, pos, val)
        else:
            self.update(node * 2 + 1, mid + 1, r, pos, val)

        # Maintain maximum gap in current segment
        self.tree[node] = max(
            self.tree[node * 2],
            self.tree[node * 2 + 1]
        )

    def query(self, node: int, l: int, r: int, ql: int, qr: int) -> int:
        # Returns maximum gap in range [ql, qr]

        if ql > r or qr < l:
            return 0

        if ql <= l and r <= qr:
            return self.tree[node]

        mid = (l + r) // 2

        return max(
            self.query(node * 2, l, mid, ql, qr),
            self.query(node * 2 + 1, mid + 1, r, ql, qr),
        )


class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:

        # Find maximum coordinate used in queries
        mx = 0
        for q in queries:
            mx = max(mx, q[1])

        # Fenwick Tree tracks occupied positions
        fw = Fenwick(mx + 2)

        # Segment Tree tracks maximum free interval lengths
        st = SegTree(mx + 1)

        # Position 0 is initially occupied
        # Stored as index 1 in Fenwick Tree
        fw.add(1, 1)

        ans: List[bool] = []

        for q in queries:
            t = q[0]
            x = q[1]

            # Type 1: Insert obstacle at position x
            if t == 1:

                # Find nearest occupied position on the left
                left_count = fw.sum(x)
                left_pos = fw.kth(left_count) - 1

                # Find nearest occupied position on the right
                occupied_up_to_x = fw.sum(x + 1)
                total_occupied = fw.sum(mx + 2)

                right_pos = -1

                if occupied_up_to_x < total_occupied:
                    right_pos = fw.kth(occupied_up_to_x + 1) - 1

                # Gap ending at x
                st.update(
                    1, 0, mx,
                    x,
                    x - left_pos
                )

                # Existing gap gets split by inserting x
                if right_pos != -1:
                    st.update(
                        1, 0, mx,
                        right_pos,
                        right_pos - x
                    )

                # Mark x as occupied
                fw.add(x + 1, 1)

            # Type 2: Check if block of size sz fits
            else:
                sz = q[2]

                # Nearest occupied position on left of x
                left_count = fw.sum(x)
                left_pos = fw.kth(left_count) - 1

                # Largest completed gap ending before x
                best_prefix = st.query(
                    1, 0, mx,
                    0, x
                )

                # Valid if:
                # 1. Current open interval ending at x is large enough
                # OR
                # 2. Any previous gap is large enough
                ans.append(
                    (x - left_pos >= sz)
                    or
                    (best_prefix >= sz)
                )

        return ans