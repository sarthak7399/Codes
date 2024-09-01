# https://www.geeksforgeeks.org/problems/swapping-pairs-make-sum-equal4142/

# Input: n = 6, m = 4, a[] = {4, 1, 2, 1, 1, 2}, b[] = (3, 6, 3, 3)
# Output: 1
# Explanation: Sum of elements in a[] = 11, Sum of elements in b[] = 15, To get same sum from both arrays, we can swap following values: 1 from a[] and 3 from b[]

class Solution:
    def findSwapValues(self,a, n, b, m):
        # Your code goes here
        sum_a, sum_b = sum(a), sum(b)
        diff = sum_a - sum_b
        
        # If the difference is odd, we cannot find two integers (one from each array) 
        # that satisfy the condition because (a[i] - b[j]) must be an integer
        if diff % 2 != 0:
            return -1
        
        # sum_a - a[i] + b[j] = sum_b - b[j] + a[i]
        # 2 * (a[i] - b[j]) = sum_a - sum_b
        # a[i] - b[j] = diff = (sum_a - sum_b) / 2
        
        target = diff // 2
        
        set_a = set(a)
        set_b = set(b)
        
        for num in set_a:
            if (num - target) in set_b:
                return 1
        
        return -1