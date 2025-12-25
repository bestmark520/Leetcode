// 58. Length of Last Word Solved // c++

class Solution {
public:
    int lengthOfLastWord(string s) {
        int n = s.size();
        int count = 0;
        for (int i = (n - 1); i > -1;i--){
            if (s[i] != ' ')
                count += 1;
            else if (count != 0)
                return count;
        }
        return count;
    }
};