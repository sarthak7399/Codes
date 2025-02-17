# https://leetcode.com/problems/letter-tile-possibilities/

# Example 1:
# Input: tiles = "AAB"
# Output: 8
# Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        # Initialize an array to store the frequency of each letter (A-Z)
        counts = [0] * 26  
        
        # Precompute factorial values for permutations
        fac = [1] * (len(tiles) + 1)  
        for i in range(1, len(tiles) + 1):
            fac[i] = i * fac[i - 1]
        
        # Count occurrences of each letter in tiles
        for c in tiles:
            counts[ord(c) - ord('A')] += 1  
        
        # Array to store the number of ways to form sequences of different lengths
        lengthcounts = [0] * (len(tiles) + 1)
        lengthcounts[0] = 1  # There's one way to form an empty sequence
        
        # Iterate over all possible characters
        for i in range(26):
            if counts[i] > 0:  # If a letter is present in tiles
                temp = [0] * (len(tiles) + 1)  # Temporary array for updates
                
                # Iterate over possible sequence lengths
                for j in range(len(tiles) + 1):
                    if lengthcounts[j] > 0:  # If there is a valid sequence of length j
                        
                        # Try adding 1 to counts[i] occurrences of the current letter
                        for k in range(1, counts[i] + 1):  
                            totallength = j + k  # New total length
                            
                            # Compute number of ways to arrange this sequence
                            temp[totallength] += lengthcounts[j] * fac[totallength] // (fac[k] * fac[j])
                
                # Update lengthcounts with new possibilities
                for j in range(len(tiles) + 1):
                    lengthcounts[j] += temp[j]
        
        # Sum up all possibilities excluding the empty sequence
        return sum(lengthcounts[1:])