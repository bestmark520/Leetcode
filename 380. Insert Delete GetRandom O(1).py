# 380. Insert Delete GetRandom O(1) # python

import random

class RandomizedSet(object):

    def __init__(self):
        self.nums = []
        self.nums_dict = {}

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.nums_dict:
            return False
        else:
            self.nums.append(val)
            self.nums_dict[val] = len(self.nums) - 1
            return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.nums_dict:
            return False
        else:
            exchange_place = self.nums_dict[val]
            self.nums_dict[self.nums[-1]] = exchange_place
            self.nums[exchange_place], self.nums[exchange_place] = self.nums[len(self.nums) - 1], self.nums[
                len(self.nums) - 1]
            self.nums.pop()
            del self.nums_dict[val]
            return True

    def getRandom(self):
        """
        :rtype: int
        """
        if len(self.nums) == 0:
            return False
        else:
            return random.choice(self.nums)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

'''
# dict(hash table)的架構
list = [1]
dict = {1: 0}
dict = {value: key（index)}
dict = {名字： 學號}

# 插入 1
nums.append(1)
num_to_index[1] = len(nums) - 1  # {1: 0}
# 插入數字到dict = 插入同學到班級
dict[名字] = 學號
dict[劉高甸] = R12945070
但dict可以多個名字對一樣的學號
dict{x, y}：x對y可以一對一、多對一，不能一對多

# 舉例刪除掉3
list = [1, 2, 3, 4, 5]
dict = {1:0, 2:1, 3:2, 4:3, 5:4}

step1:
exchange_place = self.nums_dict[val]
self.nums_dict[self.nums[-1]] = exchange_place
list = [1, 2, 3, 4, 5]
dict = {1:0, 2:1, 3:2, 4:3, 5:2}

step2:
self.nums[exchange_place], self.nums[exchange_place] = self.nums[len(self.nums) - 1], self.nums[len(self.nums) - 1]
list = [1, 2, 5, 4, 3]
dict = {1:0, 2:1, 3:2, 4:3, 5:2}

step3:
self.nums.pop()
del self.nums_dict[val]
list = [1, 2, 5, 4]
dict = {1:0, 2:1, 4:3, 5:2}
所以刪除後會引響list的順序

# 比對時間複雜度
leetcode_380_dict的學號對應list的位子
if val in dict:  O(1)
if val in list:  O(n)
'''

'''
def remove(self, val):  # 另一種寫法
    if val == self.nums[-1]:
            self.nums.pop()
            del self.nums_dict[val]
            return True
        else:
            exchange_place = self.nums_dict[val]
            last_list = self.nums[-1]
            self.nums[exchange_place] = last_list
            self.nums.pop()
            del self.nums_dict[val]
            self.nums_dict[last_list] = exchange_place
            return True
'''
