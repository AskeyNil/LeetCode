'''
Description: 最长公共前缀
Author: AskeyNil
CreateDate: 2019-08-30 21:50:56
LastEditors: AskeyNil

********************************
**                            **
**   It works on my machine   **
**                            **
********************************

'''

"""
'     编写一个函数来查找字符串数组中的最长公共前缀。
' 如果不存在公共前缀，返回空字符串 ""。
'
' 示例 1:
' 输入: ["flower","flow","flight"]
' 输出: "fl"
'
' 示例 2:
' 输入: ["dog","racecar","car"]
' 输出: ""
' 解释: 输入不存在公共前缀。
'
' 说明:
' 所有输入只包含小写字母 a-z 。
"""

# ! ######################   START   ##########################


class Solution:
    def longestCommonPrefix(self, strs) -> str:
        index = 0
        common = ""
        while True:
            temp_chars = map(lambda s: s[index:index+1], strs)
            temp_set = set(temp_chars)
            if len(temp_set) == 1:
                temp_str = temp_set.pop()
                if temp_str:
                    common += temp_str
                    index += 1
                    continue
            break
        return common


print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))
