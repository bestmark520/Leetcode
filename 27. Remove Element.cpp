// 27. Remove Element  // c++

class Solution {
public:
    int removeElement(vector<int>& nums, int val) {

        for(int i = nums.size()-1; i > -1; i = i-1 ){
            if (nums[i] == val){
                 nums.erase(nums.begin() + i);
            }
        }
    return nums.size();
    }
};