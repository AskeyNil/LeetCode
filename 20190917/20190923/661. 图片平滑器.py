'''
Description: 图片平滑器
Author: AskeyNil
CreateDate: 2019-09-23 14:22:13
LastEditors: AskeyNil

*********************************
**                             **
**     　  你只有足够努力     　  **
**       才能看上去毫不费力       **
**                             **
*********************************

'''


# 算是暴力破解了
# 只是用了偏移量来简化判断
class Solution:
    def imageSmoother(self, M: [[int]]) -> [[int]]:
        m_h = len(M)
        m_v = len(M[0])
        # 设置偏移数组
        direction = [(-1, -1), (0, -1), (1, -1),
                     (-1, 0), (0, 0), (1, 0),
                     (-1, 1), (0, 1), (1, 1)]
        re = []
        for i, N in enumerate(M):
            re.append([])
            for j, n in enumerate(N):
                sum_n = 0
                count = 0
                for h, v in direction:
                    # 实际位置
                    h1 = i + h
                    if h1 < 0 or h1 >= m_h:
                        continue
                    v1 = j + v
                    if v1 < 0 or v1 >= m_v:
                        continue
                    sum_n += M[h1][v1]
                    count += 1
                re[i].append(sum_n // count)
        return re
