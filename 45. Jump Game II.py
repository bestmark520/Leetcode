# 45. Jump Game II # python

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 不能無腦擴張領土就+1
        # 要有一個邊界，那個邊界內的都是step多少以內能到的
        # nums[0]是step0
        # 其中step0最遠能到的區域都是step1
        # 假如step0最遠能到nums[3]，那nums[1:3] = step1
        # 再看step1最遠能到多少
        # 假如step1最遠到nums[10]，那nums[4:10] = step2
        max_range = 0
        step = 0
        last_step_line = 0
        max_line = len(nums) - 1
        for i in range(len(nums)):
            if last_step_line >= max_line:
                return step
            max_range = max(max_range, i + nums[i])
            if i == last_step_line:  # 當i = last_step_line = 0時，進入step1
                step += 1
                last_step_line = max_range  # step1的範圍是1~0+nums[0]
