'''
Description: 整数反转
Author: AskeyNil
CreateDate: 2019-08-27 08:23:09
LastEditors: AskeyNil

********************************
**                            **
**   It works on my machine   **
**                            **
********************************

'''

"""
'     给出一个 32 位的有符号整数，你需要将这个整数中每位上
' 的数字进行反转。
'
' 示例 1:
' 输入: 123
' 输出: 321
'
' 示例 2:
' 输入: -123
' 输出: -321
'
' 示例 3:
' 输入: 120
' 输出: 21
'
' 注意:
'     假设我们的环境只能存储得下 32 位的有符号整数，则其数
' 值范围为 [−2^31,  2^31 − 1]。请根据这个假设，如果反转后整
' 数溢出那么就返回 0。

"""


# ! ######################   START   ##########################

class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        # 将负数和正数分开处理, 数字反转但是符号不反转
        if "-" in s:
            x = int("-" + s[1:][::-1])
        else:
            x = int(s[::-1])
        if x < - (2 ** 31) or x > 2 ** 31 - 1:
            return 0
        return x
