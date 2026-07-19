# https://leetcode.com/problems/maximum-profit-from-trading-stocks-with-discounts/

# Example 1:
# Input: n = 2, present = [1,2], future = [4,3], hierarchy = [[1,2]], budget = 3
# Output: 5
# Explanation:
# Employee 1 buys the stock at price 1 and earns a profit of 4 - 1 = 3.
# Since Employee 1 is the direct boss of Employee 2, Employee 2 gets a discounted price of floor(2 / 2) = 1.
# Employee 2 buys the stock at price 1 and earns a profit of 3 - 1 = 2.
# The total buying cost is 1 + 1 = 2 <= budget. Thus, the maximum total profit achieved is 3 + 2 = 5.

class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        # Build adjacency list for hierarchy tree
        adj_list = defaultdict(list)
        for h in hierarchy:
            adj_list[h[0] - 1].append(h[1] - 1)
        
        @lru_cache(None)
        def dfs(employee, has_discount):
            # Cost with/without discount
            cost = present[employee] // 2 if has_discount else present[employee]
            profit = future[employee] - cost
            
            # Option 1: buy current employee stock
            buy_current = {cost: profit} if cost <= budget else {}
            # Option 2: skip current employee
            skip_current = {0: 0}
            
            for child in adj_list[employee]:
                # Child results with and without discount
                child_with_discount = dfs(child, True)
                child_no_discount = dfs(child, False)
                
                # Combine results when buying current
                new_buy = {}
                for spent, prof in buy_current.items():
                    for child_spent, child_prof in child_with_discount.items():
                        total_spent = spent + child_spent
                        if total_spent <= budget:
                            total_prof = prof + child_prof
                            if total_spent not in new_buy or new_buy[total_spent] < total_prof:
                                new_buy[total_spent] = total_prof
                buy_current = new_buy
                
                # Combine results when skipping current
                new_skip = {}
                for spent, prof in skip_current.items():
                    for child_spent, child_prof in child_no_discount.items():
                        total_spent = spent + child_spent
                        if total_spent <= budget:
                            total_prof = prof + child_prof
                            if total_spent not in new_skip or new_skip[total_spent] < total_prof:
                                new_skip[total_spent] = total_prof
                skip_current = new_skip
            
            # Merge buy and skip results
            result = {}
            for spent, prof in buy_current.items():
                if spent not in result or result[spent] < prof:
                    result[spent] = prof
            for spent, prof in skip_current.items():
                if spent not in result or result[spent] < prof:
                    result[spent] = prof
            
            return result
        
        # Start DFS from root with no discount
        result = dfs(0, False)
        return max(result.values()) if result else 0
