// 26. Remove Duplicates from Sorted Array // c++

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.empty()) return 0;
        int k = 1;  // 下個不重複數字要放的位置
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] != nums[i - 1]) {
                nums[k] = nums[i];  // in-place 覆寫
                k++;
            }
        }
        return k;
    }
};