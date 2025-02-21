// 134. Gas Station //c++

class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int total_tank = 0;
        int current_tank = 0;
        int start_index = 0;

        for (int i =0; i< gas.size(); i++){
            total_tank += gas[i] - cost[i];
            current_tank += gas[i] - cost[i];

            // 若目前的油量不足，重新選擇起點
            if (current_tank < 0){
                start_index = i + 1;
                current_tank = 0; // 重置當前油量 //不用重置total
            }
        }
        if (total_tank >= 0){
            return start_index;
        }
        else {
            return -1;
        }

    }
};