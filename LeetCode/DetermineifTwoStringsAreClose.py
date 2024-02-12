# https://leetcode.com/problems/determine-if-two-strings-are-close/description/?envType=study-plan-v2&envId=leetcode-75&__cf_chl_tk=HyYodGpGHXln3lCBwgSgMz5Mt5F17V1WwKfbVKqTu9I-1706898763-0-gaNycGzNElA

# Example 1:
# Input: word1 = "abc", word2 = "bca"
# Output: true
# Explanation: You can attain word2 from word1 in 2 operations.
# Apply Operation 1: "abc" -> "acb"
# Apply Operation 1: "acb" -> "bca"

# Example 2:
# Input: word1 = "a", word2 = "aa"
# Output: false
# Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.

# METHOD 1 :
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        def countFrequency(my_list) -> dict:
            freq = {}
            for item in my_list:
                freq[item] = freq.get(item, 0) + 1
            return freq
        
        if len(word1) != len(word2):
            return False

        freq1 = countFrequency(word1)
        freq2 = countFrequency(word2)

        if set(freq1.keys()) != set(freq2.keys()):
            return False

        return sorted(freq1.values()) == sorted(freq2.values())


# METHOD 2 (Although Similar approach, takes less time because sets are made earlier.):
# class Solution:
#     def closeStrings(self, word1: str, word2: str) -> bool:
#         if len(word1) != len(word2):
#             return False

#         set1, set2 = set(word1), set(word2)
        
#         if set1 != set2:
#             return False
#         elif len(set1) == len(word1):   # Single Character Check - If they are equal, it means that word1 contains only unique characters, and hence it is "close" to word2.
#             return True
            
#         store1 = []
#         store2 = []
#         for i in set1:
#             store1.append(word1.count(i))
#             store2.append(word2.count(i))

#         return sorted(store1) == sorted(store2)