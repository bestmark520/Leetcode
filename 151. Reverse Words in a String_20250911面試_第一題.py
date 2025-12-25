class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        result = [""] * (n+1)
        count = 0
        position = n
        for i in range(n+1):
            if i == n or s[i] == " ":
                length = count
                if length > 0:
                    position -= length
                    for j in range(length):
                        result[position+j] = s[i-length+j] # 把最前面的You放到最後面
                    position -= 1
                    if position >= 0:
                        result[position] = " " # 在You的前面補一個空格
                    count = 0
            else:
                count += 1
        return "".join(result).strip()

solution = Solution()
print(solution.reverseWords("You are very smart"))
