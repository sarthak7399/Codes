# https://leetcode.com/problems/sum-of-prefix-scores-of-strings/

# Example 1:
# Input: words = ["abc","ab","bc","b"]
# Output: [5,4,3,2]
# Explanation: The answer for each string is the following:
# - "abc" has 3 prefixes: "a", "ab", and "abc".
# - There are 2 strings with the prefix "a", 2 strings with the prefix "ab", and 1 string with the prefix "abc".
# The total is answer[0] = 2 + 2 + 1 = 5.
# - "ab" has 2 prefixes: "a" and "ab".
# - There are 2 strings with the prefix "a", and 2 strings with the prefix "ab".
# The total is answer[1] = 2 + 2 = 4.
# - "bc" has 2 prefixes: "b" and "bc".
# - There are 2 strings with the prefix "b", and 1 string with the prefix "bc".
# The total is answer[2] = 2 + 1 = 3.
# - "b" has 1 prefix: "b".
# - There are 2 strings with the prefix "b".
# The total is answer[3] = 2.

class Node:
    def __init__(self):
        self.count = 0
        self.list = [None] * 26

    def containKey(self, ch):
        return self.list[ord(ch) - ord('a')] is not None

    def get(self, ch):
        return self.list[ord(ch) - ord('a')]

    def put(self, ch, new_node):
        self.list[ord(ch) - ord('a')] = new_node

    def inc(self, ch):
        self.list[ord(ch) - ord('a')].count += 1

    def retCount(self, ch):
        return self.list[ord(ch) - ord('a')].count


class Solution:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        node = self.root
        for ch in word:
            if not node.containKey(ch):
                node.put(ch, Node())
            node.inc(ch)
            node = node.get(ch)

    def search(self, word):
        node = self.root
        preCount = 0
        for ch in word:
            preCount += node.retCount(ch)
            node = node.get(ch)
        return preCount

    def sumPrefixScores(self, words):
        # This problem can be solved using the trie data structure
        for word in words:
            self.insert(word)

        res = []
        for word in words:
            preCount = self.search(word)
            res.append(preCount)

        return res