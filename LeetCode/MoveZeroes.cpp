// https://leetcode.com/problems/move-zeroes/description/?envType=study-plan-v2&envId=leetcode-75

// Input: nums = [0,1,0,3,12]
// Output: [1,3,12,0,0]

#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        vector<int> temp(nums.size(),0);
        int k=0;
        for(int i=0;i<nums.size();i++){
            if(nums[i]!=0){
                temp[k++]=nums[i];
            }
        }
        nums=temp;
    }
};