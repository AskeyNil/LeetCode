'''
Description: 正则表达式匹配
Author: AskeyNil
CreateDate: 2019-08-28 18:34:49
LastEditors: AskeyNil

********************************
**                            **
**   It works on my machine   **
**                            **
********************************

'''

"""
'     给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 
' 的正则表达式匹配。
' '.' 匹配任意单个字符
' '*' 匹配零个或多个前面的那一个元素
' 所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。
'
' 说明:
' s 可能为空，且只包含从 a-z 的小写字母。
' p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
'
' 示例 1:
' 输入:
' s = "aa"
' p = "a"
' 输出: false
' 解释: "a" 无法匹配 "aa" 整个字符串。
'
' 示例 2:
' 输入:
' s = "aa"
' p = "a*"
' 输出: true
' 解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
'
' 示例 3:
' 输入:
' s = "ab"
' p = ".*"
' 输出: true
' 解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
'
' 示例 4:
' 输入:
' s = "aab"
' p = "c*a*b"
' 输出: true
' 解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
'
' 示例 5:
' 输入:
' s = "mississippi"
' p = "mis*is*p*."
' 输出: false
"""


# ! ######################   START   ##########################


# class Reg:
#     def __init__(self, char, more=False):
#         self.char = char
#         self.more = more
#         self.start_index = 0
#         self.end_index = 0
#         self.str = ""

#     def __eq__(self, value):
#         if self.char == ".":
#             return self.more == value.more
#         return self.char == value.char and self.more == value.more

#     def match(self, s: str, start_index: int) -> int:
#         count = 0
#         self.str = s
#         self.start_index = start_index
#         if self.more:
#             for char in s[start_index:]:
#                 if char == self.char or self.char == ".":
#                     count += 1
#                 else:
#                     break
#         else:
#             if self.char == s[start_index:start_index + 1] or self.char == ".":
#                 count += 1
#         self.end_index = start_index + count
#         return count

#     def pop(self) -> str:
#         if self.more:
#             self.end_index -= 1
#             return self.str[self.end_index - 1:self.end_index]
#         return ""


# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:
#         '''
#         @description: 自定义正则匹配(. *)
#         @params:
#             - s: 输入的字符串
#             - p: 正则规则
#         @return: 匹配是否成功 bool
#         '''
#         len_p = len(p)
#         len_s = len(s)
#         i = 0
#         p_arr = []
#         index = 0
#         while i < len_p:
#             if p[i+1:i+2] == "*":
#                 r = Reg(p[i:i+1], True)
#                 p_arr.append(r)
#                 i += 2
#             else:
#                 r = Reg(p[i:i+1], False)
#                 p_arr.append(r)
#                 i += 1

#             r_index = r.match(s, index)
#             if r_index == 0:
#                 j = -2
#                 if len(p_arr) == 1:
#                     j = -1
#                 else:
#                     while j >= -len(p_arr):
#                         p_arr[j].more
#                         if p_arr[j].more and p_arr[j].end_index != p_arr[j].start_index:
#                             break
#                         j -= 1
#                     if j < -len(p_arr):
#                         if not r.more:
#                             return False
#                         else:
#                             continue
#                 if p_arr[j].char == r.char or p_arr[j].char == ".":
#                     if p_arr[j].end_index > p_arr[j].start_index:
#                         if p_arr[j].pop() != r.char:
#                             if not r.more:
#                                 return False
#                     else:
#                         if not r.more:
#                             return False
#                 else:
#                     if not r.more:
#                         return False
#             index += r_index
#         return index >= len_s


class Solution(object):
    def isMatch(self, text, pattern):
        if not pattern:
            return not text
        first_match = bool(text) and pattern[0] in {text[0], '.'}
        if len(pattern) >= 2 and pattern[1] == '*':
            return (self.isMatch(text, pattern[2:]) or
                    first_match and self.isMatch(text[1:], pattern))
        else:
            return first_match and self.isMatch(text[1:], pattern[1:])


print(Solution().isMatch("bbbba", "a"))
