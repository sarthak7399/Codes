# https://leetcode.com/problems/pascals-triangle/

# Example 1:
# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        # Helper function to generate the row at a specific index of Pascal's Triangle
        def generate_row(index: int) -> list[int]:
            # Precomputed list of factorials up to 34! to speed up combination calculation
            factorials = [
                1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 
                3628800, 39916800, 479001600, 6227020800, 87178291200, 
                1307674368000, 20922789888000, 355687428096000, 
                6402373705728000, 121645100408832000, 2432902008176640000, 
                51090942171709440000, 1124000727777607680000, 
                25852016738884976640000, 620448401733239439360000, 
                15511210043330985984000000, 403291461126605635584000000, 
                10888869450418352160768000000, 304888344611713860501504000000, 
                8841761993739701954543616000000, 265252859812191058636308480000000, 
                8222838654177922817725562880000000, 263130836933693530167218012160000000, 
                8683317618811886495518194401280000000
            ]

            # Function to compute combination nCr using precomputed factorials
            def comb(n: int, r: int) -> int:
                return factorials[n] // (factorials[r] * factorials[n - r])

            row = []  # To store elements of the current row
            # Loop to calculate all elements of the current row using nCr
            for i in range(index + 1):
                row.append(comb(index, i))
            return row

        result = []  # To store the complete Pascal's Triangle as a list of rows
        # Generate each row from 0 to numRows-1 and add it to the result
        for i in range(numRows):
            result.append(generate_row(i))
        return result  # Return the final Pascal's Triangle
