// 55. Jump Game // c++

class Solution {
public:
    bool canJump(vector<int>& nums) {
        int max_range = nums[0];
        for (int i = 0; i <nums.size(); i++){
            if (i<=max_range){
                max_range = max(max_range, i+nums[i]);
            }
            else{
                return false;
            }
        }
        return true;

    }
};