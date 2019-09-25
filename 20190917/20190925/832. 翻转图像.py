'''
Description: 翻转图像
Author: AskeyNil
CreateDate: 2019-09-25 09:25:37
LastEditors: AskeyNil

*********************************
**                             **
**     　  你只有足够努力     　  **
**       才能看上去毫不费力       **
**                             **
*********************************

'''


class Solution:
    def flipAndInvertImage(self, A: [[int]]) -> [[int]]:
        arr = [[0 for _ in range(len(A))] for _ in range(len(A))]
        i = 0
        for N in A:
            j = 0
            for n in N[::-1]:
                if n == 0:
                    arr[i][j] = 1
                j += 1
            i += 1
        return arr
