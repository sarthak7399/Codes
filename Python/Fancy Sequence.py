# https://leetcode.com/problems/fancy-sequence/

# Example 1:
# Input
# ["Fancy", "append", "addAll", "append", "multAll", "getIndex", "addAll", "append", "multAll", "getIndex", "getIndex", "getIndex"]
# [[], [2], [3], [7], [2], [0], [3], [10], [2], [0], [1], [2]]
# Output
# [null, null, null, null, null, 10, null, null, null, 26, 34, 20]
# Explanation
# Fancy fancy = new Fancy();
# fancy.append(2);   // fancy sequence: [2]
# fancy.addAll(3);   // fancy sequence: [2+3] -> [5]
# fancy.append(7);   // fancy sequence: [5, 7]
# fancy.multAll(2);  // fancy sequence: [5*2, 7*2] -> [10, 14]
# fancy.getIndex(0); // return 10
# fancy.addAll(3);   // fancy sequence: [10+3, 14+3] -> [13, 17]
# fancy.append(10);  // fancy sequence: [13, 17, 10]
# fancy.multAll(2);  // fancy sequence: [13*2, 17*2, 10*2] -> [26, 34, 20]
# fancy.getIndex(0); // return 26
# fancy.getIndex(1); // return 34
# fancy.getIndex(2); // return 20

class Fancy:

    def __init__(self):
        # Modulo value used in the problem
        self.mod = 10**9 + 7
        
        # Stores the normalized values of the sequence
        self.val = []
        
        # Global multiplier (represents multiplication operations)
        self.a = 1
        
        # Global increment (represents addition operations)
        self.b = 0

    def append(self, val: int) -> None:
        # When appending, we reverse the current transformation
        # Current transformation applied to elements:
        # final_value = a * stored_value + b
        
        # To store a value correctly, we compute the reverse:
        # stored_value = (val - b) / a
        
        # (val - b) mod mod
        x = (val - self.b + self.mod) % self.mod
        
        # Multiply by modular inverse of a to divide by a under modulo
        self.val.append(x * pow(self.a, self.mod - 2, self.mod) % self.mod)

    def addAll(self, inc: int) -> None:
        # Adding to all elements means increasing the global increment
        self.b = (self.b + inc) % self.mod

    def multAll(self, m: int) -> None:
        # Multiplying all elements affects both multiplier and increment
        self.a = (self.a * m) % self.mod
        self.b = (self.b * m) % self.mod

    def getIndex(self, idx: int) -> int:
        # If index is out of bounds
        if idx >= len(self.val):
            return -1
        
        # Apply the transformation to get the actual value
        # final_value = a * stored_value + b
        return (self.a * self.val[idx] + self.b) % self.mod


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)