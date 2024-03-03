# https://leetcode.com/problems/koko-eating-bananas/description/?envType=study-plan-v2&envId=leetcode-75&__cf_chl_tk=HyYodGpGHXln3lCBwgSgMz5Mt5F17V1WwKfbVKqTu9I-1706898763-0-gaNycGzNElA

# Example 1:
# Input: piles = [3,6,7,11], h = 8
# Output: 4

# Example 2:
# Input: piles = [30,11,23,4,20], h = 5
# Output: 30


from typing import List
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)     # Initialize search space
        ans = right
        while left <= right:
            mid = (left + right) // 2
            hours = 0           
            for bananas in piles:        # Calculate total hours required to eat all bananas at the current speed
                hours += (bananas + mid - 1) // mid
            if hours <= h:      # Update answer if the current speed allows all bananas to be eaten within h hours
                ans = min(ans, mid)
                right = mid - 1     # Explore lower eating speeds
            else:
                left = mid + 1      # Explore higher eating speeds
        return ans      