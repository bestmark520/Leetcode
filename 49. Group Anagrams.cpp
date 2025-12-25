class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> anagrams;
        for (string s : strs) {
            string key = s;
            sort(key.begin(), key.end());   // 將字串排序
            anagrams[key].push_back(s);     // 加入對應群組
        }

        // 將 hash map 的值轉成 vector<vector<string>>
        vector<vector<string>> result;
        for (auto &pair : anagrams) {
            result.push_back(pair.second);
        }
        return result;
    }
};