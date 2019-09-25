'''
Description: 至少是其他数字两倍的最大数
Author: AskeyNil
CreateDate: 2019-09-25 07:45:18
LastEditors: AskeyNil

*********************************
**                             **
**     　  你只有足够努力     　  **
**       才能看上去毫不费力       **
**                             **
*********************************

'''


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        i = -1
        max_number = None
        for index, num in enumerate(nums):
            if max_number == None:
                i = index
                max_number = num
            else:
                if max_number < num:
                    max_number = num
                    if max_number * 2 < num:
                        i = index
                    else:
                        i = -1
        return i
