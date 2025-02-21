// 189. Rotate Array // c++

class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        while (nums.size()<k){
            k = k-nums.size();
        }
        vector<int> v1;
        for (int i = nums.size()-1-k+1; i<nums.size(); i++){
            v1.insert(v1.end(), nums[i]);
        }
        for (int j = 0;j<nums.size()-1-k+1;j++){
            v1.insert(v1.end(),nums[j]);
        }
        nums = v1;
    }
};