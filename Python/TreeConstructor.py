# Create a function named treeConstructor that takes an array of strings, strArr, as input. Each string in strArr represents a pair of integers in the format "(i1,i2)", where i1 denotes a child node in a tree and i2 signifies its parent. Your task is to determine whether the pairs of integers can form a valid binary tree.
# The function should return true if a valid binary tree can be constructed using the pairs, and false otherwise. Note that all integers within the tree are unique, implying that each node in the tree can have only one parent.

# Example Test Cases:

# 1-- Input: ["(1,2)", "(2,4)", "(5,7)", "(7,2)", "(9,5)"]
# Output: true
# Explanation: The pairs form the following tree:

# 2-- Input: ["(1,2)", "(3,2)", "(2,12)", "(5,2)"]
# Output: false
# Explanation: The pairs cannot form a valid binary tree since node 2 has two children (1 and 3), violating the binary tree property.

# 3-- Input: ["(1,2)", "(2,4)", "(5,7)", "(7,2)", "(9,5)"]
# Output: false
# Explanation: The pairs do not form a valid binary tree due to the presence of a cycle in the tree structure.

# Ensure that your function efficiently handles different input scenarios and accurately determines whether the provided pairs can construct a valid binary tree.

def TreeConstructor(strArr): 
    strArr = [eval(entry) for entry in strArr]
    parents = [y for x, y in strArr]
    children = [x for x, y in strArr]
    if sum([0 if entry in children else 1 for entry in set(parents)]) != 1:
        return 'false'
    if any([parents.count(y)>2 for y in parents]):
        return 'false'
    return 'true'