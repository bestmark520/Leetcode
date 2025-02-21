// 13. Roman to Integer Solved // c++

class Solution {
public:
    int romanToInt(string s) {
        unordered_map<char, int> s_dict = {
            {'I', 1},
            {'V', 5},
            {'X', 10},
            {'L', 50},
            {'C', 100},
            {'D', 500},
            {'M', 1000},
        };
        int sum = s_dict[s[s.size()-1]];
        for (int i = 0; i < s.size()-1; i++){
            if (s_dict[s[i]]< s_dict[s[i+1]]){
                sum -= s_dict[s[i]];
            }
            else {
                sum += s_dict[s[i]];
            }
        }
        return sum;
    }
};