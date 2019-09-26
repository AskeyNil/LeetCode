'''
Description: 转置矩阵
Author: AskeyNil
CreateDate: 2019-09-26 08:11:12
LastEditors: AskeyNil

*********************************
**                             **
**     　  你只有足够努力     　  **
**       才能看上去毫不费力       **
**                             **
*********************************

'''


class Solution:
    def transpose(self, A: [[int]]) -> [[int]]:
        line_number = len(A)
        column_number = len(A[0])
        re_result = [[0 for _ in range(line_number)]
                     for _ in range(column_number)]
        for x, line in enumerate(re_result):
            for y, item in enumerate(line):
                re_result[x][y] = A[y][x]
        return re_result
