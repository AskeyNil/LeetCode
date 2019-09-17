'''
Description: 最长回文子串
Author: AskeyNil
CreateDate: 2019-08-26 09:28:00
LastEditors: AskeyNil

********************************
**                            **
**   It works on my machine   **
**                            **
********************************

'''

"""
'    给定一个字符串 s，找到 s 中最长的回文子串。
' 你可以假设 s 的最大长度为 1000。
'
' 示例 1：
' 输入: "babad"
' 输出: "bab"
' 注意: "aba" 也是一个有效答案。
'
' 示例 2：
' 输入: "cbbd"
' 输出: "bb"
"""

# ! ######################   START   ##########################


# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         temp_s = ""
#         max_str = s[0:1]
#         max_str_len = 1
#         for index, char in enumerate(s):
#             if char in temp_s:
#                 temp_s += char
#                 temp_c = temp_s
#                 i = temp_c.find(char)
#                 if char == "r":
#                     print(temp_s + " ")
#                 while i != -1:
#                     temp_c = temp_c[i:]

#                     if temp_c == temp_c[::-1]:  # 当前的数是回文子串
#                         if len(temp_c) > max_str_len:

#                             max_str = temp_c
#                             max_str_len = len(temp_c)
#                             break
#                     if len(temp_c) < max_str_len:
#                         break
#                     i = temp_c.find(char, 1)
#             else:
#                 temp_s += char

#         return max_str


# print(Solution().longestPalindrome("civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"))


# ! ######################  动态规划   ##########################
# ! 该方法的效率大致是上面方法的 8 倍


# class Solution:
#     def longestPalindrome(self, s):
#         # 字符串长度
#         str_length = len(s)
#         # 最长的长度
#         max_length = 0
#         # 开始索引
#         start = 0
#         for i in range(str_length):
#             # ? 思想
#             # ? 先查找子序列
#             # ? 当前的 max_length 其实是最长长度 -1
#             # ? 开始的是否查找一个含有两个元素的子串,然后查找一个三个元素的子串
#             # ? 然后因为 max_length 增加 所以查找的子串长度也随之增加,小的子串便不再考虑
#             if i - max_length >= 1 and s[i - max_length - 1:i + 2] == s[i - max_length - 1:i + 2][::-1]:
#                 start = i - max_length - 1
#                 max_length += 2
#                 continue
#             if i - max_length >= 0 and s[i - max_length:i + 2] == s[i - max_length:i + 2][::-1]:
#                 start = i - max_length
#                 max_length += 1
#         return s[start:start + max_length+1]


# print(Solution().longestPalindrome("dadabccacd"))


# ! ######################   马拉车算法   ##########################
class Solution:
    def longestPalindrome(self, s: str):
        # 1. 将 '#' 字符插入到字符串中, 任意一个不存在于字符串中的字符均可
        temp_s = ""
        for char in s:
            temp_s += "#" + char
        temp_s += "#"

        # 已查找出的最大回文子串的中心点坐标
        max_id = 0
        # 已查找出的最大回文子串的最右点坐标
        max_right = 0
        # 存储所有位置的回文数的扩散长度, 默认为 0
        p = [0 for _ in temp_s]

        # 字符串长度
        len_s = len(temp_s)

        # 记录之前最大的数据
        current_count = 1
        current_str = s[0:1]

        for index, char in enumerate(temp_s):
            # 先试试能不能直接使用 p 去获取当前的回文数值
            if max_right > index:
                p[index] = min(p[2 * max_id - index], max_right - index)
            else:
                if index > max_right:
                    raise "程序有问题"
                p[index] = 1

            # 中心匹配
            while index - p[index] >= 0 and index + p[index] < len_s and temp_s[index - p[index]] == temp_s[index + p[index]]:
                p[index] += 1

            if index + p[index] > max_right:
                max_right = index + p[index]
                max_id = index

            if p[index] - 1 > current_count:
                current_count = p[index] - 1
                current_str = temp_s[index - p[index] +
                                     1:index + p[index]].replace("#", "")

        return current_str


print(Solution().longestPalindrome("babad"))
