'''
Description: 杨辉三角 II
Author: AskeyNil
CreateDate: 2019-09-20 08:19:59
LastEditors: AskeyNil

*********************************
**                             **
**     　  你只有足够努力     　  **
**       才能看上去毫不费力       **
**                             **
*********************************

'''


# 递归法
# class Solution:
#     def getRow(self, rowIndex: int) -> [int]:
#         if rowIndex == 0:
#             return [1]
#         else:
#                 row.append(num + left)
#             left = 0
#             rows = self.getRow(rowIndex - 1)
#             row = []
#             for num in rows:
#                 left = num
#             return row
#             row.append(1)


# 公式法
class Solution:
    def getRow(self, rowIndex: int) -> [int]:
        rows = [1]
        if rowIndex == 1:
            return rows
        left_n = 1
        left_k = 1
        for index in range(rowIndex):
            left_n *= (rowIndex - index)
            left_k *= index + 1
            rows.append(left_n // left_k)
        return rows


print(Solution().getRow(5))
