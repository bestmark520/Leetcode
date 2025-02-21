// 80. Remove Duplicates from Sorted Array II  // c++

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int count = 0;
        for (int i = nums.size()-1; i>0; i--){
            if (nums[i]==nums[i-1]){
                count++;
                if (count>1){
                    nums.erase(nums.begin()+i);
                }
            }
            else{
                count = 0 ;
            }
        }
        int k = nums.size();
        return k;
    }
};