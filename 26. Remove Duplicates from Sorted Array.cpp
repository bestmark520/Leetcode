// 26. Remove Duplicates from Sorted Array // c++


class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        vector<int> v1;
        for (int i = nums.size()-1;i>0;i=i-1){
            if (nums[i-1]==nums[i]){
                v1.push_back(i);
            }
        }
        for (int j : v1) {  // 同 python的 for j in error:
            nums.erase(nums.begin()+ j );
        }
        int k = nums.size();
        return k;
    }
};