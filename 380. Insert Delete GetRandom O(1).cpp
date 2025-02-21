// 380. Insert Delete GetRandom O(1) // c++

class RandomizedSet {
private:
    //  std:: 就是python的.self，這裡沒有使用
    vector<int> nums;
    unordered_map<int, int> nums_dict;  // unordered_map就是宣告一個dict

public:
    RandomizedSet() {

    }

    bool insert(int val) {
        if (nums_dict.find(val) != nums_dict.end()) // != .end() 不在.end()表示存在
        {
            return false;
        }
        else {
            nums.push_back(val);
            nums_dict[val] = nums.size() - 1;
            return true;
        }

    }

    bool remove(int val) {
         if (nums_dict.find(val) == nums_dict.end()) // == .end() 表示不存在
        {
            return false;
        }
        else {
            int exchange_place = nums_dict[val];
            nums_dict[nums.back()] = exchange_place;
            swap(nums[exchange_place], nums.back());  // 交換
            nums.pop_back();
            nums_dict.erase(val);
            return true;
        }

    }

    int getRandom() {
        if (nums.empty()) {
            return false;
        }
        else {
            return nums[std::rand() % nums.size()];
        }
    }


};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet* obj = new RandomizedSet();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */