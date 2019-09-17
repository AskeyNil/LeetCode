'''
Description: 无重复字符的最长子串
Author: AskeyNil
CreateDate: 2019-08-25 21:33:08
LastEditors: AskeyNil

********************************
**                            **
**   It works on my machine   **
**                            **
********************************

'''

"""
'     给定一个字符串，请你找出其中不含有重复字符的
' 最长子串 的长度。
'
' 示例 1:
' 输入: "abcabcbb"
' 输出: 3
' 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

' 示例 2:
' 输入: "bbbbb"
' 输出: 1
' 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

' 示例 3:
' 输入: "pwwkew"
' 输出: 3
' 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。

! 请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

"""

# ! ######################   START   ##########################


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp_str = ""
        max_number = 0
        for index, char in enumerate(s):
            if char in temp_str:
                i = temp_str.index(char)
                max_number = max(len(temp_str), max_number)
                temp_str = temp_str[i+1:]
            temp_str += char
        max_number = max(len(temp_str), max_number)
        return max_number


print(Solution().lengthOfLongestSubstring("abcabcbb"))
