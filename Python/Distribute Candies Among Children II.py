# https://leetcode.com/problems/distribute-candies-among-children-ii/

# Example 1:
# Input: n = 5, limit = 2
# Output: 3
# Explanation: There are 3 ways to distribute 5 candies such that no child gets more than 2 candies: (1, 2, 2), (2, 1, 2) and (2, 2, 1).

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        # Computes the number of combinations to choose 2 elements from x (C(x,2) = x*(x-1)//2)
        # Returns 0 if x < 2 (since we can't choose 2 elements)
        def C2(x: int) -> int:
            return (x * (x - 1) // 2) if x >= 2 else 0

        # Total number of non-negative integer solutions to a + b + c = n
        # (Using stars and bars formula: C(n + 3 - 1, 3 - 1) = C(n + 2, 2))
        total = (n + 2) * (n + 1) // 2

        # Count of solutions where one variable (say a) exceeds the limit
        # If a > limit, then a = limit + 1 + x → a + b + c = n becomes x + b + c = n - (limit + 1)
        x1 = n - limit + 1
        t1 = C2(x1)

        # Count of solutions where two variables (say a and b) exceed the limit
        # a = b = limit + 1 + x → x + x + c = n - 2*(limit + 1)
        x2 = n - 2 * limit
        t2 = C2(x2)

        # Count of solutions where all three variables exceed the limit
        # a = b = c = limit + 1 + x → 3x = n - 3*(limit + 1)
        x3 = n - 3 * limit - 1
        t3 = C2(x3)

        # Use Inclusion-Exclusion Principle:
        # Subtract over-limit cases:
        #   - Subtract cases where at least one exceeds the limit (3 * t1)
        #   - Add back overcounted pairs (a and b both exceeded: 3 * t2)
        #   - Subtract again for triple overcount (all a, b, c exceed limit: t3)
        return total - 3 * t1 + 3 * t2 - t3
