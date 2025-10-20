# https://leetcode.com/problems/lexicographically-smallest-string-after-applying-operations/

# Example 1:
# Input: s = "5525", a = 9, b = 2
# Output: "2050"
# Explanation: We can apply the following operations:
# Start:  "5525"
# Rotate: "2555"
# Add:    "2454"
# Add:    "2353"
# Rotate: "5323"
# Add:    "5222"
# Add:    "5121"
# Rotate: "2151"
# Add:    "2050"​​​​​
# There is no way to obtain a string that is lexicographically smaller than "2050".

from collections import deque

class Solution(object):
    def findLexSmallestString(self, s, a, b):
        """
        Find lexicographically smallest string after applying operations
        Strategy: BFS to explore all reachable string states
        
        Operations:
        1. Add 'a' to all digits at odd indices (mod 10)
        2. Rotate string right by 'b' positions
        
        :type s: str - initial string of digits
        :type a: int - value to add to odd-indexed digits
        :type b: int - number of positions to rotate
        :rtype: str - lexicographically smallest reachable string
        """
        
        # 📊 Initialize variables
        l = len(s)              # Cache length for efficiency
        q = deque([s])          # BFS queue - start with initial string
        seen = set([s])         # Track visited states to avoid cycles
        res = s                 # Best (smallest) result found so far
        
        # 🔄 BFS: Explore all reachable string states
        while q:
            # 🎯 Get next state to explore (LIFO - using pop())
            # Note: Could use popleft() for true BFS, but order doesn't matter
            # since we're finding minimum across ALL states
            curr = q.pop()
            
            # 📊 Check if current state is better than best so far
            # String comparison is lexicographic by default
            if curr < res:
                res = curr      # Update best result
            
            # ✨ OPERATION 1: Add 'a' to all odd-indexed digits
            # Convert string to list for mutability
            temp = list(curr)
            
            # Iterate through odd indices: 1, 3, 5, ...
            for i in range(1, l, 2):
                # Add 'a' to digit and wrap around using mod 10
                # Example: (9 + 3) % 10 = 2
                temp[i] = str((int(temp[i]) + a) % 10)
            
            # Convert list back to string
            temp_s = ''.join(temp)
            
            # ✅ If this state is new, explore it
            if temp_s not in seen:
                seen.add(temp_s)    # Mark as visited
                q.append(temp_s)    # Add to queue for exploration
            
            # 🔄 OPERATION 2: Rotate string right by 'b' positions
            # Python slicing: curr[-b:] gets last b chars
            #                 curr[:-b] gets all but last b chars
            # Example: "5525" with b=2 → "25" + "55" = "2555"
            rotated = curr[-b:] + curr[:-b]
            
            # ✅ If this rotated state is new, explore it
            if rotated not in seen:
                seen.add(rotated)   # Mark as visited
                q.append(rotated)   # Add to queue for exploration
        
        # 🎯 Return the lexicographically smallest string found
        return res


# 🎓 Algorithm Walkthrough Example:
#
# Input: s = "5525", a = 9, b = 2
#
# Initial: q = ["5525"], seen = {"5525"}, res = "5525"
#
# BFS Exploration Tree (partial):
#
#                    "5525"
#                   /      \
#              (add 9)    (rotate 2)
#                /           \
#            "5425"         "2555"
#            /    \         /    \
#        (add)  (rot)   (add)  (rot)
#         /      \       /      \
#     "5335"  "2554" "2455"  "5525" (seen!)
#       /  \     ...     ...
#     ...  ...
#
# Process Flow:
# 1. Start: "5525"
#    → Add 9 to odd: "5425" ✅
#    → Rotate by 2: "2555" ✅
#
# 2. Process "5425" (new best!)
#    → res = "5425"
#    → Add 9 to odd: "5335" ✅
#    → Rotate by 2: "2554" ✅
#
# 3. Process "2555" (new best!)
#    → res = "2555"
#    → Add 9 to odd: "2455" ✅
#    → Rotate by 2: "5525" (seen, skip)
#
# 4. Continue exploring all states...
#    Eventually finds: "2050" ✨
#
# 5. Queue empty → return "2050"
#
# 🔑 Why This Works:
#
# 1. **Complete Exploration:** BFS visits all reachable states
# 2. **Cycle Prevention:** 'seen' set prevents infinite loops
# 3. **Optimal Tracking:** Always keep track of smallest string
# 4. **State Graph:** Each string is a node, operations are edges
#
# 🚀 Key Insights:
# - State space is finite (limited by string transformations)
# - BFS guarantees we explore all possibilities
# - Lexicographic comparison finds global minimum
# - Two operations can be applied in any order/combination
#
# 🎯 The beauty: Simple BFS finds optimal solution! ⚡