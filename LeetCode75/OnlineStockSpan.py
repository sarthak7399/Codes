# https://leetcode.com/problems/online-stock-span/description/?envType=study-plan-v2&envId=leetcode-75&__cf_chl_tk=HyYodGpGHXln3lCBwgSgMz5Mt5F17V1WwKfbVKqTu9I-1706898763-0-gaNycGzNElA

# Example 1:
# Input:
# ["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
# [[], [100], [80], [60], [70], [60], [75], [85]]
# Output:
# [null, 1, 1, 1, 2, 1, 4, 6]
# Explanation
# StockSpanner stockSpanner = new StockSpanner();
# stockSpanner.next(100); // return 1
# stockSpanner.next(80);  // return 1
# stockSpanner.next(60);  // return 1
# stockSpanner.next(70);  // return 2
# stockSpanner.next(60);  // return 1
# stockSpanner.next(75);  // return 4, because the last 4 prices (including today's price of 75) were less than or equal to today's price.
# stockSpanner.next(85);  // return 6

class StockSpanner:
    def __init__(self):
        self.stack=[]   # Stack to store prices and their corresponding spans
        
    def next(self, price: int) -> int:
        curr_span=1     # Span starts from 1
        while self.stack and self.stack[-1][0]<=price:      # If the price is less than or equal to the top of the stack, pop the top of the stack and add the span
            prev_price,prev_span=self.stack.pop()       # Pop the top of the stack
            curr_span+=prev_span        # Add the span
        self.stack.append((price,curr_span))        # Append the price and span
        return curr_span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)