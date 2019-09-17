'''
Description: 有效的括号
Author: AskeyNil
CreateDate: 2019-09-07 21:31:18
LastEditors: AskeyNil

********************************
**                            **
**   It works on my machine   **
**                            **
********************************

'''

"""
'    给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
' 有效字符串需满足：
'   左括号必须用相同类型的右括号闭合。
'   左括号必须以正确的顺序闭合。
'   注意空字符串可被认为是有效字符串。
'
' 示例 1:
' 输入: "()"
' 输出: true
'
' 示例 2:
' 输入: "()[]{}"
' 输出: true
'
' 示例 3:
' 输入: "(]"
' 输出: false
'
' 示例 4:
' 输入: "([)]"
' 输出: false
'
' 示例 5:
' 输入: "{[]}"
' 输出: true
"""

# ! ######################   START   ##########################


class Solution:
    def isValid(self, s: str) -> bool:
        dic = {")": "(",
               "]": "[",
               "}": "{"}
        line = []
        for char in s:
            if char in dic:
                if not line or line.pop() != dic[char]:
                    return False
            else:
                line.append(char)
        return not line


print(Solution().isValid("]"))
