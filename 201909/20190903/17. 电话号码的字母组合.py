'''
Description: 电话号码的字母组合
Author: AskeyNil
CreateDate: 2019-09-02 22:40:14
LastEditors: AskeyNil

********************************
**                            **
**   It works on my machine   **
**                            **
********************************

'''
"""
'     给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
' 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
'   2 -> a b c,  3 -> d e f, 4 -> g h i,
'   5 -> j k l,  6 -> m n o, 7 -> p q r s,
'   8 -> t u v,  9 -> w x y z
'
' 示例:
'
' 输入："23"
' 输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
' 说明:
' 尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。
"""


# ! ######################   START   ##########################


class Solution:
    def letterCombinations(self, digits: str) -> [str]:
        dic = {"2": ["a", "b", "c"],
               "3": ["d", "e", "f"],
               "4": ["g", "h", "i"],
               "5": ["j", "k", "l"],
               "6": ["m", "n", "o"],
               "7": ["p", "q", "r", "s"],
               "8": ["t", "u", "v"],
               "9": ["w", "x", "y", "z"]}
        l = list(digits)
        temp = []
        for char in l:
            temp = self.multiply(temp, dic[char])
        return temp

    def multiply(self, x: [str], y: [str]):
        temp = []
        if x and y:
            for i in x:
                for j in y:
                    temp.append(i + j)
        else:
            if x:
                temp = x
            elif y:
                temp = y
        return temp


print(Solution().letterCombinations("23"))


# 几乎等于穷举法
