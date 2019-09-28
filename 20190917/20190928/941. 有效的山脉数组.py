'''
Description: 有效的山脉数组
Author: AskeyNil
CreateDate: 2019-09-28 08:02:08
LastEditors: AskeyNil

*********************************
**                             **
**     　  你只有足够努力     　  **
**       才能看上去毫不费力       **
**                             **
*********************************

'''


class Solution:
    def validMountainArray(self, A: [int]) -> bool:
        is_down = False
        left = None
        length = len(A)
        for index, num in enumerate(A):
            if left is None:
                left = num
            else:
                if is_down:
                    if left < num:
                        return False
                else:
                    if left > num:
                        if index < 2:
                            return False
                        is_down = True
                    if index == length - 1:
                        return False
        return True
