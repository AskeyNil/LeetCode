'''
Description: 单调数列
Author: AskeyNil
CreateDate: 2019-09-26 09:18:45
LastEditors: AskeyNil

*********************************
**                             **
**     　  你只有足够努力     　  **
**       才能看上去毫不费力       **
**                             **
*********************************

'''


class Solution:
    def isMonotonic(self, A: [int]) -> bool:
        length = len(A)
        if length < 3:
            return True
        left = 0
        for index in range(length - 1):
            if left == 0:
                if A[index + 1] - A[index] > 0:
                    left = 1
                elif A[index + 1] - A[index] < 0:
                    left = -1
            elif left == 1:
                if A[index + 1] - A[index] < 0:
                    return False
            else:
                if A[index + 1] - A[index] > 0:
                    return False
        return True
