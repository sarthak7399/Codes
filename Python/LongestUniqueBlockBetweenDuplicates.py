# Have the function StringChallenge(str) take the str parameter being passed and determine the largest number of unique characters that exists between a pair of matching letters anywhere in the string. For example: if str is "ahyjakh" then there are only two pairs of matching letters, the two a's and the two h's. Between the pair of a's there are 3 unique characters: h, y, and j. Between the h's there are 4 unique characters: y, j, a, and k. So for this example your program should return 4.

# Another example: if str is "ghececgkaem" then your program should return 5 because the most unique characters exists within the farthest pair of e characters. The input string may not contain any character pairs, and in that case your program should just return 0. The input will only consist of lowercase alphabetic characters.
# Examples
# Input: "mmmerme"
# Output: 3

def StringChallenge(strParam):
    max_unique = 0
    for i in range(len(strParam)):
        for j in range(i+1, len(strParam)):
            if strParam[i] == strParam[j]:
                unique_chars = len(set(strParam[i+1:j]))
                max_unique = max(max_unique, unique_chars)
    return max_unique

# Test the function with example inputs
print(StringChallenge("ahyjakh"))  # Output: 4
# print(StringChallenge("ghececgkaem"))  # Output: 5
# print(StringChallenge("mmmerme"))  # Output: 3