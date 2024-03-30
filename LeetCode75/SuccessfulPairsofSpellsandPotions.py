# https://leetcode.com/problems/successful-pairs-of-spells-and-potions/description/?envType=study-plan-v2&envId=leetcode-75&__cf_chl_tk=HyYodGpGHXln3lCBwgSgMz5Mt5F17V1WwKfbVKqTu9I-1706898763-0-gaNycGzNElA

# Example 1:
# Input: spells = [5,1,3], potions = [1,2,3,4,5], success = 7
# Output: [4,0,3]
# Explanation:
# - 0th spell: 5 * [1,2,3,4,5] = [5,10,15,20,25]. 4 pairs are successful.
# - 1st spell: 1 * [1,2,3,4,5] = [1,2,3,4,5]. 0 pairs are successful.
# - 2nd spell: 3 * [1,2,3,4,5] = [3,6,9,12,15]. 3 pairs are successful.
# Thus, [4,0,3] is returned.

# Example 2:
# Input: spells = [3,1,2], potions = [8,5,8], success = 16
# Output: [2,0,2]
# Explanation:
# - 0th spell: 3 * [8,5,8] = [24,15,24]. 2 pairs are successful.
# - 1st spell: 1 * [8,5,8] = [8,5,8]. 0 pairs are successful. 
# - 2nd spell: 2 * [8,5,8] = [16,10,16]. 2 pairs are successful. 
# Thus, [2,0,2] is returned.


from typing import List
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        res = [0] * len(spells)  # Initialize a result list with zeros
        potions.sort()  # Sort the potions list in ascending order

        for i in range(len(spells)):        
            needed = success // spells[i] + bool(success % spells[i])  # find the smallest value to reach in spells
            l, r = 0, len(potions)  # Initialize pointers for binary search
            while l < r:
                mid = l + (r - l) // 2  # Calculate the middle index
                if potions[mid] < needed:
                    l = mid + 1  # Adjust the left pointer if the value is less than needed
                else:
                    r = mid  # Adjust the right pointer otherwise
                res[i] = len(potions) - l  # Store the count of successful pairs
        return res  # Return the result list