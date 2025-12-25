// 238. Product of Array Except Self Solved // c++

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> answer(n, 1);
        int start = 1;
        for (int i=0; i< n - 1; i++){
            start *= nums[i];
            answer[i + 1] *= start;
        }
        start = 1;
        for (int i=(n - 1); i> 0; i--){
            start *= nums[i];
            answer[i - 1] *= start;
        }
        return answer;
    }
};