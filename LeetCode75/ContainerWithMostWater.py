# https://leetcode.com/problems/container-with-most-water/description/?envType=study-plan-v2&envId=leetcode-75&__cf_chl_tk=HyYodGpGHXln3lCBwgSgMz5Mt5F17V1WwKfbVKqTu9I-1706898763-0-gaNycGzNElA

# Example 1:
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49

#     0         0   
#     1         0   1
#     1 0       0   1
#     1 0   0   0   1
#     1 0   0 0 0   1
#     1 0   0 0 0   1
#     1 0 0 0 0 0 0 1
#   0 1 0 0 0 0 0 0 1
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 

from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxWater,i,j = 0, 0, len(height)-1
        temp=min(height[i],height[j])*(j-i)
        while(i<len(height)-1 and j>=0):
            temp=min(height[i],height[j])*(j-i)
            if(height[i]<height[j] and temp<=maxWater): 
                i+=1
            elif(height[i]>=height[j] and temp<=maxWater): 
                j-=1
            maxWater=max(maxWater, temp)
            # print(maxWater, i , j)
        return maxWater