// 274. H-Index Attempted // c++

class Solution {
public:
    int hIndex(vector<int>& citations) {
        int h_score = 0;
        for (int i=1; i<citations.size() + 1;i++){
            int count = 0;
            for (int j:citations){
                if (j >= i){
                    count += 1;
                }
                if (count >= i){
                    h_score = max(h_score, i);
                }
            }
        }
        return h_score;
    }
};