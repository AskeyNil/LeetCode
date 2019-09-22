'''
Description: 第三大的数
Author: AskeyNil
CreateDate: 2019-09-22 18:36:57
LastEditors: AskeyNil

*********************************
**                             **
**     　  你只有足够努力     　  **
**       才能看上去毫不费力       **
**                             **
*********************************

'''


class Solution:
    def thirdMax(self, nums: [int]) -> int:
        nums = list(set(nums))
        nums.sort()
        if len(nums) >= 3:
            return nums[-3]
        else:
            return nums[-1]
