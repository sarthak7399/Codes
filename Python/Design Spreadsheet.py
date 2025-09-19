# https://leetcode.com/problems/design-spreadsheet/

# Example 1:
# Input:
# ["Spreadsheet", "getValue", "setCell", "getValue", "setCell", "getValue", "resetCell", "getValue"]
# [[3], ["=5+7"], ["A1", 10], ["=A1+6"], ["B2", 15], ["=A1+B2"], ["A1"], ["=A1+B2"]]
# Output:
# [null, 12, null, 16, null, 25, null, 15]
# Explanation
# Spreadsheet spreadsheet = new Spreadsheet(3); // Initializes a spreadsheet with 3 rows and 26 columns
# spreadsheet.getValue("=5+7"); // returns 12 (5+7)
# spreadsheet.setCell("A1", 10); // sets A1 to 10
# spreadsheet.getValue("=A1+6"); // returns 16 (10+6)
# spreadsheet.setCell("B2", 15); // sets B2 to 15
# spreadsheet.getValue("=A1+B2"); // returns 25 (10+15)
# spreadsheet.resetCell("A1"); // resets A1 to 0
# spreadsheet.getValue("=A1+B2"); // returns 15 (0+15)

class Spreadsheet:
    def __init__(self, rows: int):
        # Dictionary to store cell values
        # Key = cell name (like "A1"), Value = integer stored in that cell
        self.map = {}

    def setCell(self, cell: str, value: int) -> None:
        # Assign a value to the given cell
        # Example: setCell("A1", 10) → stores {"A1": 10}
        self.map[cell] = value

    def resetCell(self, cell: str) -> None:
        # Reset (delete) a cell if it exists in the spreadsheet
        if cell in self.map:
            del self.map[cell]

    def getValue(self, formula: str) -> int:
        # Formula format: "=X+Y" (where X and Y can be either
        #   - a cell reference like "A1", or
        #   - a direct number like "5")
        # Example: "=A1+10" or "=3+7"

        # Find the position of '+'
        i = formula.index("+")

        # Extract the two parts (ignoring the leading '=')
        cell1 = formula[1:i]      # left part after '=' up to '+'
        cell2 = formula[i+1:]     # right part after '+'

        # Get value for cell1:
        #   - If it starts with a letter → treat as a cell name (lookup in map)
        #   - Else → treat as a number (convert to int)
        val1 = self.map.get(cell1, 0) if cell1[0].isalpha() else int(cell1)

        # Same logic for cell2
        val2 = self.map.get(cell2, 0) if cell2[0].isalpha() else int(cell2)

        # Return sum of the two operands
        return val1 + val2
