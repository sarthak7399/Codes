# https://leetcode.com/problems/count-good-triplets-in-an-array/

# Example 1:
# Input: nums1 = [2,0,1,3], nums2 = [0,1,2,3]
# Output: 1
# Explanation: 
# There are 4 triplets (x,y,z) such that pos1x < pos1y < pos1z. They are (2,0,1), (2,0,3), (2,1,3), and (0,1,3). 
# Out of those triplets, only the triplet (0,1,3) satisfies pos2x < pos2y < pos2z. Hence, there is only 1 good triplet.

class Solution:
    def goodTriplets(self, nums1, nums2):
        n = len(nums1)
        
        # Create a position mapping of each number in nums2
        pos = [0] * n
        for i in range(n):
            pos[nums2[i]] = i
        
        # Map nums1 to the index positions based on nums2
        # This converts nums1 into a permutation that reflects positions in nums2
        nums1 = [pos[x] for x in nums1]

        # Two Binary Indexed Trees (Fenwick Trees)
        bit1 = [0] * (n + 2)  # For prefix counts
        bit2 = [0] * (n + 2)  # For counts of valid 2-length sequences

        # BIT update operation: add 'val' at index 'i'
        def update(bit, i, val):
            i += 1  # BIT is 1-indexed
            while i <= n :
                bit[i] += val
                i += i & -i

        # BIT query operation: sum from index 0 to i
        def query(bit, i):
            i += 1
            res = 0
            while i > 0:
                res += bit[i]
                i -= i & -i
            return res

        ans = 0
        # Traverse nums1 in reverse to build good triplets from the back
        for i in reversed(range(n)):
            x = nums1[i]

            # Count how many numbers to the right of x are greater than x (for second position in triplet)
            val = query(bit1, n - 1) - query(bit1, x)

            # Count how many valid (second, third) pairs can be formed with x as the first element
            trip = query(bit2, n - 1) - query(bit2, x)

            # Accumulate the total number of good triplets
            ans += trip

            # Update BITs: x can now be used as a second element in a pair
            update(bit2, x, val)  # Contribute val pairs where x is the second element
            update(bit1, x, 1)    # Mark x as seen in bit1

        return ans
