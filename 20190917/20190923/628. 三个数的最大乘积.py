'''
Description: 三个数的最大乘积
Author: AskeyNil
CreateDate: 2019-09-23 11:57:36
LastEditors: AskeyNil

*********************************
**                             **
**     　  你只有足够努力     　  **
**       才能看上去毫不费力       **
**                             **
*********************************

'''


class Solution:
    def maximumProduct(self, nums: [int]) -> int:
        # 排序
        nums.sort()
        # 取最后三个数
        max_number = nums[-1] * nums[-2] * nums[-3]
        # 取前面两个和最后一个乘积 因为有可能有负数
        min_number = nums[0] * nums[1] * nums[-1]
        return max_number if max_number > min_number else min_number
