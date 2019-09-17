'''
Description: Z 字形变换
Author: AskeyNil
CreateDate: 2019-08-26 12:13:32
LastEditors: AskeyNil

********************************
**                            **
**   It works on my machine   **
**                            **
********************************

'''

"""
'     将一个给定字符串根据给定的行数，以从上往下、从左到右
' 进行 Z 字形排列。比如输入字符串为 "LEETCODEISHIRING" 
' 行数为 3 时，排列如下：
'
'           L   C   I   R
'           E T O E S I I G
'           E   D   H   N
'     之后，你的输出需要从左往右逐行读取，产生出一个新的字
' 符串，比如："LCIRETOESIIGEDHN"。
'
' 示例 1:
' 输入: s = "LEETCODEISHIRING", numRows = 3
' 输出: "LCIRETOESIIGEDHN"
'
' 示例 2:
' 输入: s = "LEETCODEISHIRING", numRows = 4
' 输出: "LDREOEIIECIHNTSG"
' 解释:
'           L     D     R
'           E   O E   I I
'           E C   I H   N
'           T     S     G
"""

# ! ######################   START   ##########################


# ! 找规律进行求解
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        return_str = ""
        if numRows == 1:
            return s
        base_process = 2 * (numRows - 1)
        for index in range(numRows):
            if index == 0 or index == numRows - 1:
                return_str += s[index::2 * (numRows - 1)]
            else:
                return_str += self.process(s, index, base_process)
        return return_str

    def process(self, s, index, base_process):
        first = base_process - 2 * index
        second = 2 * index
        is_first = True
        return_str = ""
        while index < len(s):
            return_str += s[index]
            if is_first:
                index += first
            else:
                index += second
            is_first = not is_first
        return return_str


print(Solution().convert("0123456", 3))
