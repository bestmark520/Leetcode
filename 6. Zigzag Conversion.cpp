// 6. Zigzag Conversion // c++

class Solution {
public:
    string convert(string s, int numRows) {

        if (numRows == 1)
            return s;

        int n = s.size();
        vector<string> ans_(numRows, ""); // 建立 numRows 個空字串
        int cycle = numRows * 2 - 2;

        for (int i = 0; i < n; i++) {
            int x = i % cycle;
            if (x >= numRows) {
                x = cycle - x;
            }
            ans_[x] += s[i];
        }

        string result = "";
        for (const string& rowStr : ans_) {
            result += rowStr;
        }

        return result;

    }
};