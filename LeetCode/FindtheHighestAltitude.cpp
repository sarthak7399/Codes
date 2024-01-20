// https://leetcode.com/problems/find-the-highest-altitude/?envType=study-plan-v2&envId=leetcode-75

// Input: gain = [-5,1,5,0,-7]
// Output: 1
// Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.

#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        int ans=0,i;
        vector<int> vect2;
        for (int i=0; i<gain.size(); i++)  
            vect2.push_back(gain[i]); 
        for(i=1;i<gain.size();i++){
            vect2[i]=vect2[i]+vect2[i-1];
        }
        for(i=0;i<gain.size();i++){
            if(ans<vect2[i]){
                ans=vect2[i];
            }
        }
        return ans;
    }
};