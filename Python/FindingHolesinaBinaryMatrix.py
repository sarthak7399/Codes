# Have the function SearchingChallenge(strArr) take the array of strings stored in strArr, which will be a 2D matrix of 0 and 1's, and determine how many holes, or contiguous regions of 0's, exist in the matrix. A contiguous region is one where there is a connected group of 0's going in one or more of four directions: up, down, left, or right. For example: if strArr is ["10111", "10101", "11101", "11111"], then this looks like the following matrix:

# 1 0 1 1 1
# 1 0 1 0 1
# 1 1 1 0 1
# 1 1 1 1 1

# For the input above, your program should return 2 because there are two separate contiguous regions of 0's, which create "holes" in the matrix. You can assume the input will not be empty.
# Examples
# Input: ["01111", "01101", "00011", "11110"]
# Output: 3

def SearchingChallenge(strArr):
    # Convert the array of strings to a 2D matrix of integers
    matrix = [list(map(int, row)) for row in strArr]
    
    # Define directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    def dfs(x, y):
        # Mark the current cell as visited
        matrix[x][y] = 1
        
        # Explore all four directions
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            # Check if the new position is within the bounds and is a 0
            if 0 <= new_x < len(matrix) and 0 <= new_y < len(matrix[0]) and matrix[new_x][new_y] == 0:
                dfs(new_x, new_y)
    
    hole_count = 0
    
    # Iterate through each cell in the matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                # If the current cell is 0 and unvisited, perform DFS to explore the contiguous region
                dfs(i, j)
                # Increment the hole count after DFS
                hole_count += 1
                
    return hole_count

# Test the function with example inputs
print(SearchingChallenge(["01111", "01101", "00011", "11110"]))  # Output: 3
