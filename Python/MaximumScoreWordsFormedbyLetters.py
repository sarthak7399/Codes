# https://leetcode.com/problems/maximum-score-words-formed-by-letters/

# Example 1:
# Input: words = ["dog","cat","dad","good"], letters = ["a","a","c","d","d","d","g","o","o"], score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
# Output: 23
# Explanation:
# Score  a=1, c=9, d=5, g=3, o=2
# Given letters, we can form the words "dad" (5+1+5) and "good" (3+2+2+5) with a score of 23.
# Words "dad" and "dog" only get a score of 21.

from typing import List
class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        n = len(words)
        res = 0

        # count letters
        letters_count = [0 for _ in range(26)]
        for letter in letters:
            ind = ord(letter) - 97
            letters_count[ind] += 1
        
        # calculate words
        words_scores = {}
        for word in words:
            s = 0
            for char in word:
                ind = ord(char) - 97
                s += score[ind]
            words_scores[word] = s
 
        for mask in range(0, 2 ** n, 1): # There will be exactly 2^n different states
            cur_count = [0 for _ in range(26)]
            can_create = True
            cur_score = 0

            for word_ind in range(n):
                if (mask & (1 << word_ind)) != 0: # if in mask bit of this word is 1
                    word = words[word_ind]
                    cur_score += words_scores[word]
                    for char in word:
                        ind = ord(char) - 97
                        cur_count[ind] += 1
                        if cur_count[ind] > letters_count[ind]:
                            can_create = False
                            break
                if not can_create:
                    break
            if can_create and cur_score > res: 
                res = cur_score

        return res