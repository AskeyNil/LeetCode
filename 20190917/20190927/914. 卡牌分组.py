'''
Description: 卡牌分组
Author: AskeyNil
CreateDate: 2019-09-26 22:33:51
LastEditors: AskeyNil

*********************************
**                             **
**     　  你只有足够努力     　  **
**       才能看上去毫不费力       **
**                             **
*********************************

'''


class Solution:
    def hasGroupsSizeX(self, deck):
        dic = {}
        for num in deck:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
        g = -1
        # 获取出现次数
        for v in dic.values():
            if g == -1:
                g = v
            else:
                g = self.gcd(g, v)
        return g >= 2

    def gcd(self, x, y):
        return y if x == 0 else self.gcd(y % x, x)


print(Solution().hasGroupsSizeX(
    [1, 1, 1, 2, 2, 2, 3, 3]))
