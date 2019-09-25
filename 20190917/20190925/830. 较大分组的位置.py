'''
Description: 较大分组的位置
Author: AskeyNil
CreateDate: 2019-09-25 08:55:57
LastEditors: AskeyNil

*********************************
**                             **
**     　  你只有足够努力     　  **
**       才能看上去毫不费力       **
**                             **
*********************************

'''


class Solution:
    def largeGroupPositions(self, S: str) -> [[int]]:
        left = None
        leftIndex = -1
        arr = []
        for index, c in enumerate(S):
            if left == None:
                left = c
                leftIndex = index
            elif c != left:
                if index - leftIndex >= 3:
                    arr.append([leftIndex, index - 1])
                leftIndex = index
                left = c
        if len(S) - leftIndex >= 3:
            arr.append([leftIndex, len(S) - 1])
        return arr
