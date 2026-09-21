# https://leetcode.com/problems/find-x-value-of-array-i/

# Example 1:
# Input: nums = [1,2,3,4,5], k = 3
# Output: [9,2,4]
# Explanation:
# For x = 0, the possible operations include all possible ways to remove non-overlapping prefix/suffix that do not remove nums[2] == 3.
# For x = 1, the possible operations are:
# Remove the empty prefix and the suffix [2, 3, 4, 5]. nums becomes [1].
# Remove the prefix [1, 2, 3] and the suffix [5]. nums becomes [4].
# For x = 2, the possible operations are:
# Remove the empty prefix and the suffix [3, 4, 5]. nums becomes [1, 2].
# Remove the prefix [1] and the suffix [3, 4, 5]. nums becomes [2].
# Remove the prefix [1, 2, 3] and the empty suffix. nums becomes [4, 5].
# Remove the prefix [1, 2, 3, 4] and the empty suffix. nums becomes [5].

class Solution:
    def resultArray(self, nums, k):
        # Length of the input array.
        n = len(nums)

        # Only the remainder modulo k matters for the product.
        nums = [x % k for x in nums]

        # res[req] will store the number of subarrays
        # whose product modulo k is equal to req.
        res = [0] * k

        # Calculate the answer separately for every required
        # product remainder from 0 to k - 1.
        for req in range(k):
            # Memoization dictionary.
            # dp[(i, prevProd)] stores the number of valid subarrays
            # that can be formed starting from index i when the
            # current product is prevProd.
            dp = {}

            def solve(i, prevProd):
                # Reached the end of the array.
                if i >= n:
                    return 0

                # Return the previously calculated result if available.
                if (i, prevProd) in dp:
                    return dp[(i, prevProd)]

                # Number of ways when skipping the current element.
                skip = 0

                # Number of ways when taking the current element.
                take = 0

                # If no subarray has been started yet, we can skip
                # the current element and remain in the initial state.
                if prevProd == k:
                    skip = solve(i + 1, k)

                # Calculate the product after taking nums[i].
                if prevProd == k:
                    # Start a new subarray with nums[i].
                    curProd = nums[i]
                else:
                    # Extend the existing subarray and keep only
                    # the product modulo k.
                    curProd = (prevProd * nums[i]) % k

                # Count the current subarray if its product
                # matches the required remainder.
                take += 1 if curProd == req else 0

                # Continue extending the subarray from the next index.
                take += solve(i + 1, curProd)

                # Store the total number of possibilities for this state.
                dp[(i, prevProd)] = take + skip

                return dp[(i, prevProd)]

            # Count subarrays whose product modulo k equals req.
            res[req] = solve(0, k)

        # Return the count for every possible product remainder.
        return res