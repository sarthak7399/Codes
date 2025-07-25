# https://leetcode.com/problems/product-of-the-last-k-numbers/

# Example:

# Input
# ["ProductOfNumbers","add","add","add","add","add","getProduct","getProduct","getProduct","add","getProduct"]
# [[],[3],[0],[2],[5],[4],[2],[3],[4],[8],[2]]

# Output
# [null,null,null,null,null,null,20,40,0,null,32]

# Explanation
# ProductOfNumbers productOfNumbers = new ProductOfNumbers();
# productOfNumbers.add(3);        // [3]
# productOfNumbers.add(0);        // [3,0]
# productOfNumbers.add(2);        // [3,0,2]
# productOfNumbers.add(5);        // [3,0,2,5]
# productOfNumbers.add(4);        // [3,0,2,5,4]
# productOfNumbers.getProduct(2); // return 20. The product of the last 2 numbers is 5 * 4 = 20
# productOfNumbers.getProduct(3); // return 40. The product of the last 3 numbers is 2 * 5 * 4 = 40
# productOfNumbers.getProduct(4); // return 0. The product of the last 4 numbers is 0 * 2 * 5 * 4 = 0
# productOfNumbers.add(8);        // [3,0,2,5,4,8]
# productOfNumbers.getProduct(2); // return 32. The product of the last 2 numbers is 4 * 8 = 32 

class ProductOfNumbers:
    def __init__(self):
        self.list = []  # Stores cumulative product
        self.prod = 1   # Running product

    def add(self, num: int) -> None:
        if num == 0:  # Reset if 0 is added
            self.list = []
            self.prod = 1
        else:
            self.prod *= num  # Multiply with running product
            self.list.append(self.prod)

    def getProduct(self, k: int) -> int:
        if len(self.list) < k:  # Not enough elements
            return 0
        if len(self.list) == k:  # Directly return the product
            return self.list[-1]
        return self.list[-1] // self.list[-k - 1]  # Compute product of last k elements
