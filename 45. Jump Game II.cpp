// 45. Jump Game II // c++

class Solution {
public:
    int jump(vector<int>& nums) {
        int max_range = 0;
        int step = 0;
        int last_step_line = 0;
        int max_line = nums.size()-1;

        for (int i = 0; i < nums.size();i++){
            if (last_step_line >= max_line){
                return step; // return沒有寫在函式最後，隨便return一個0就好
            }
            max_range = max(max_range, i + nums[i]);
            if (i==last_step_line){
                step++;
                last_step_line = max_range;
            }
        }
        return 0;
    }
};

class Solution2 {
public:
    int jump2(vector<int>& nums) {
        int max_range = 0;
        int step = 0;
        int last_step_line = 0;
        int max_line = nums.size()-1;
        int final_step = 0;
        int final_done = 0;

        for (int i = 0; i < nums.size();i++){
            if (last_step_line >= max_line and final_done==0){
                final_done++;
                final_step = step;
            }
            max_range = max(max_range, i + nums[i]);
            if (i==last_step_line){
                step++;
                last_step_line = max_range;
            }
        }
        return final_step;
    }
};