# https://leetcode.com/problems/minimum-distance-to-type-a-word-using-two-fingers/

# Example 1:
# Input: word = "CAKE"
# Output: 3
# Explanation: Using two fingers, one optimal way to type "CAKE" is: 
# Finger 1 on letter 'C' -> cost = 0 
# Finger 1 on letter 'A' -> cost = Distance from letter 'C' to letter 'A' = 2 
# Finger 2 on letter 'K' -> cost = 0 
# Finger 2 on letter 'E' -> cost = Distance from letter 'K' to letter 'E' = 1 
# Total distance = 3

class Solution:
    def minimumDistance(self, word: str) -> int:
        
        # Function to calculate Manhattan distance between two characters
        # Characters are mapped to a 6-column keyboard grid
        # 26 represents "no finger placed yet"
        def dist(a, b):
            if a == 26 or b == 26:
                return 0  # No cost if one finger is unused
            return abs(a // 6 - b // 6) + abs(a % 6 - b % 6)

        A = ord('A')
        
        # Convert characters to indices (A=0, B=1, ..., Z=25)
        index = [ord(c) - A for c in word]

        # dp[free] = minimum cost where one finger is at 'prev'
        # and the other finger is at position 'free'
        # 26 means the second finger is not used yet
        dp = [float('inf')] * 27
        dp[26] = 0  # Initially, second finger is unused

        # Start with the first character
        prev = index[0]

        # Process remaining characters
        for i in range(1, len(index)):
            cur = index[i]

            # Temporary DP array for this step
            new_dp = [float('inf')] * 27

            # Try all possible positions of the "free" finger
            for free in range(27):
                if dp[free] == float('inf'):
                    continue  # Skip invalid states

                # Option 1: Move the same finger (prev → cur)
                new_dp[free] = min(
                    new_dp[free],
                    dp[free] + dist(prev, cur)
                )

                # Option 2: Use the free finger (free → cur)
                # Now prev finger becomes free
                new_dp[prev] = min(
                    new_dp[prev],
                    dp[free] + dist(free, cur)
                )

            # Update DP and previous character
            dp = new_dp
            prev = cur

        # Return the minimum cost among all possible states
        return min(dp)