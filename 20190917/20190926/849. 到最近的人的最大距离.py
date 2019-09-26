'''
Description: 到最近的人的最大距离
Author: AskeyNil
CreateDate: 2019-09-26 07:35:03
LastEditors: AskeyNil

*********************************
**                             **
**     　  你只有足够努力     　  **
**       才能看上去毫不费力       **
**                             **
*********************************

'''


class Solution:
    def maxDistToClosest(self, seats: [int]) -> int:
        indeies = [-1]
        for index, seat in enumerate(seats):
            if seat == 1:
                indeies.append(index)
        indeies.append(len(seats))
        max_index = 0
        length = len(indeies)
        for index in range(length - 1):
            tempIndex = (indeies[index + 1] - indeies[index]) // 2
            if index == 0 or index == length - 2:
                tempIndex = indeies[index + 1] - indeies[index] - 1
            if indeies[index + 1] - indeies[index] > max_index:
                max_index = tempIndex
        return max_index
