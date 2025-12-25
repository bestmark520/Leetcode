// 28. Find the Index of the First Occurrence in a String // c++

class Solution {
public:
    int strStr(string haystack, string needle) {
        vector<int> answer;
        for (int i = 0; i< haystack.size(); i++){
            int count = 0;
            for (int j = i;j< haystack.size(); j++){
                if (haystack[j] == needle[count])
                    count += 1;
                else if (haystack[j] != needle[count])
                    count = 0;
                if (count == needle.size()){
                    int x = j-count+1;
                    answer.push_back(x);
                    int count = 0;
                }
            }
        }
        if (!answer.empty())
            return *min_element(answer.begin(), answer.end());
        return -1;
    }
};
