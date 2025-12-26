# https://leetcode.com/problems/greatest-sum-divisible-by-three/

# Example 1:
# Input: nums = [3,6,5,1,8]
# Output: 18
# Explanation: Pick numbers 3, 6, 1 and 8 their sum is 18 (maximum sum divisible by 3).

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        # Lists to store numbers based on remainder when divided by 3
        r1, r2 = [], []
        total = 0
        
        # Calculate total sum and separate numbers by remainder
        for x in nums:
            total += x
            if x % 3 == 1:
                r1.append(x)
            elif x % 3 == 2:
                r2.append(x)
        
        # If already divisible by 3, return total
        if total % 3 == 0:
            return total
        
        # Sort remainder lists to remove smallest numbers when needed
        r1.sort()
        r2.sort()
        
        rem = total % 3
        
        # If remainder is 1, remove smallest 1 from r1 or smallest 2 from r2
        if rem == 1:
            op1 = total - r1[0] if len(r1) >= 1 else 0
            op2 = total - r2[0] - r2[1] if len(r2) >= 2 else 0
        
        # If remainder is 2, remove smallest 1 from r2 or smallest 2 from r1
        else:  # rem == 2
            op1 = total - r2[0] if len(r2) >= 1 else 0
            op2 = total - r1[0] - r1[1] if len(r1) >= 2 else 0
        
        # Return the best valid option
        return max(op1, op2)
