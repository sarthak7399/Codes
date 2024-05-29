# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/

# Example 1:
# Input: s = "1101"
# Output: 6
# Explanation: "1101" corressponds to number 13 in their decimal representation.
# Step 1) 13 is odd, add 1 and obtain 14. 
# Step 2) 14 is even, divide by 2 and obtain 7.
# Step 3) 7 is odd, add 1 and obtain 8.
# Step 4) 8 is even, divide by 2 and obtain 4.  
# Step 5) 4 is even, divide by 2 and obtain 2. 
# Step 6) 2 is even, divide by 2 and obtain 1.  

class Solution:
    def numSteps(self, s: str) -> int:
        num=int(s,2)
        print(num)
        count = 0
        while(True):
            if(num==1): break
            if(num%2==0): num//=2
            else: num+=1
            count+=1
        return count