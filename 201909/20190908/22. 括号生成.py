'''
Description: 括号生成
Author: AskeyNil
CreateDate: 2019-09-07 22:52:40
LastEditors: AskeyNil

*********************************
**                             **
**     　  你只有足够努力     　  **
**       才能看上去毫不费力       **
**                             **
*********************************

'''


"""
'     给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所
' 有可能的并且有效的括号组合。
' 例如，给出 n = 3，生成结果为：
'
'        [
'          "((()))",
'          "(()())",
'          "(())()",
'          "()(())",
'          "()()()"
'        ]
"""


# ! ######################   START   ##########################


class Solution:
    def generateParenthesis(self, n: int) -> [str]:
        if n == 1:
            return ["()"]
        p = []
        for item in self.generateParenthesis(n - 1):
            for index, char in enumerate(item):
                c = list(item)
                c.insert(index + 1, "()")
                p.append("".join(c))
        return list(set(p))


print(Solution().generateParenthesis(3))
