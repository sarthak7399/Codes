# https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/

# Example 1:
# Input: prices = [8,4,6,2,3]
# Output: [4,2,4,2,3]
# Explanation: 
# For item 0 with price[0]=8 you will receive a discount equivalent to prices[1]=4, therefore, the final price you will pay is 8 - 4 = 4.
# For item 1 with price[1]=4 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 4 - 2 = 2.
# For item 2 with price[2]=6 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 6 - 2 = 4.
# For items 3 and 4 you will not receive any discount at all.

from typing import List
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        """
        Adjust the prices array where each price is reduced by the next 
        smaller or equal price to its right, if such a price exists.

        Args:
        prices (List[int]): List of item prices.

        Returns:
        List[int]: Modified list of prices after discounts.
        """
        stack = []  # Stack to store indices of prices
        
        for i in range(len(prices)):
            # While there are indices in the stack and the current price is less than 
            # or equal to the price at the index stored in the stack's top
            while stack and prices[stack[-1]] >= prices[i]:
                # Apply discount to the price at the index from the stack
                prices[stack.pop()] -= prices[i]
            
            # Add the current index to the stack
            stack.append(i)
        
        return prices
