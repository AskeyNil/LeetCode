'''
Description: 数组拆分 I
Author: AskeyNil
CreateDate: 2019-09-23 09:34:59
LastEditors: AskeyNil

*********************************
**                             **
**     　  你只有足够努力     　  **
**       才能看上去毫不费力       **
**                             **
*********************************

'''


class Solution:
    def arrayPairSum(self, nums: [int]) -> int:
        length = len(nums)
        nums.sort()
        sum_num = 0
        for index in range(0, length, 2):
            sum_num += nums[index]
        return sum_num
