// 42. Trapping Rain Water // c++

class Solution {
public:
    int trap(vector<int>& height) {
        int n = height.size();
        int L2R_up = height[0];
        int R2L_up = height[n - 1];
        vector<int> L2R_line (n, 0);
        vector<int> R2L_line (n, 0);
        int result_process1 = 0;
        int result_process2 = 0;
        int result = 0;

        for (int i = 0; i <n; i++){
            L2R_up = max(L2R_up, height[i]);
            L2R_line[i] = L2R_up;
        }

        for (int i =n - 1; i> -1; i--){
            R2L_up = max(R2L_up, height[i]);
            R2L_line[i] = R2L_up;
            result_process1 = min(R2L_line[i], L2R_line[i]);
            result_process2 = result_process1 - height[i];
            if (result_process2 > 0){
                result += result_process2;
            }
        }
        return result;

    }
};