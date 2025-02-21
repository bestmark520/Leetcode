// 135. Candy Solved // c++

class Solution {
public:
    int candy(vector<int>& ratings) {
        int n = ratings.size();
        vector<int> candy_L2R(n, 1);
        vector<int> candy_R2L(n, 1);
        vector<int> candy_result(n, 1);
        int sum = 0;
        for (int i =1; i <n; i++){
            if (ratings[i] > ratings[i - 1]){
                candy_L2R[i] = candy_L2R[i - 1] + 1;
            }
        }
        for (int j =n - 2; j>-1; j--){
            if (ratings[j] > ratings[j + 1]){
                candy_R2L[j] = candy_R2L[j + 1] + 1;
            }
        }
        for (int k = 0; k< n; k++){
            candy_result[k] = max(candy_L2R[k], candy_R2L[k]);
        }
        for (int x = 0; x< n; x++){
            sum += candy_result[x];
        }
        return sum;

    }
};