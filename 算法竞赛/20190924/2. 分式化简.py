'''
Description: 分式化简
Author: AskeyNil
CreateDate: 2019-09-24 22:10:54
LastEditors: AskeyNil

*********************************
**                             **
**     　  你只有足够努力     　  **
**       才能看上去毫不费力       **
**                             **
*********************************

'''


class Solution:
    def fraction(self, cont: [int]) -> [int]:
        top = None
        bottom = None
        for con in cont[::-1]:
            if top == None:
                top = con
                bottom = 1
            else:
                top, bottom = con * top + bottom, top
        # 判断是否有最大公约数
        a, b = top, bottom
        while b:
            a, b = b, a % b
    return [top // a, bottom // a]


a = 6
b = 2
while b:
    a, b = b, a % b
print(a)

# print(Solution().fraction([0, 0, 3]))
