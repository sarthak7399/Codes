// https://leetcode.com/problems/is-subsequence/?envType=study-plan-v2&envId=leetcode-75

// Example 1:
// Input: s = "abc", t = "ahbgdc"
// Output: true

// Example 2:
// Input: s = "axc", t = "ahbgdc"
// Output: false

// Order of string1 is important

#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    bool isSubsequence(string s, string t) {
        int m = s.size(), n = t.size();
        int i = 0, j = 0;
        while (i < m && j < n) {
            if (s[i] == t[j]) {
                i++;
                j++;
            } else {
                j++;
            }
        }
        return (i == m) ? true : false;
    }
};
// class Solution {
// public:
//     bool isSubsequence(string s, string t) {
//                 int n = s.length(),m=t.length();
//         int j = 0; 
//         // For index of s (or subsequence
    
//         // Traverse s and t, and
//         // compare current character
//         // of s with first unmatched char
//         // of t, if matched
//         // then move ahead in s
//         for (int i = 0; i < m and j < n; i++)
//             if (s[j] == t[i])
//                 j++;
    
//         // If all characters of s were found in t
//         return (j == n);
//         }

// };

// // If ordering is not important, We can use unordered_set
// #include<bits/stdc++.h>
// using namespace std;
 
// class Solution {
// public:
//     bool isSubsequence(string s, string t) {
//         int c=0;
//         unordered_set<char> s1;
//         for(int i=0;i<s.size();i++){
//             s1.insert(s[i]);
//         }
//         unordered_set<char> s2(s1.begin(), s1.end());
//         for(int i=0;i<t.size();i++){
//             if(s1.find(t[i])!=s1.end()){
//                 s1.erase(t[i]);
//             }
//         }
//         // for(auto itr:s2) cout<<itr<<" 2 "<<endl;
//         // for(auto itr:s1) cout<<itr<<" ";

//         if(s1.empty()) c=1;
//         return c;
//     }

// };