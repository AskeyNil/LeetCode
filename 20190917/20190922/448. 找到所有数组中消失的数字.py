'''
Description: 找到所有数组中消失的数字
Author: AskeyNil
CreateDate: 2019-09-22 19:36:07
LastEditors: AskeyNil

*********************************
**                             **
**     　  你只有足够努力     　  **
**       才能看上去毫不费力       **
**                             **
*********************************

'''


# 妙哉
class Solution:
    def findDisappearedNumbers(self, nums: [int]) -> [int]:
        rel = []
        count = len(nums)
        for index, num in enumerate(nums):
            nums[(num - 1) % count] += count
        for index, num in enumerate(nums):
            if num <= count:
                rel.append(index+1)
