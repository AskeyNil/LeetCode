'''
Description: 子数组最大平均数 I
Author: AskeyNil
CreateDate: 2019-09-23 13:11:35
LastEditors: AskeyNil

*********************************
**                             **
**     　  你只有足够努力     　  **
**       才能看上去毫不费力       **
**                             **
*********************************

'''


# 动态规划
class Solution:
    def findMaxAverage(self, nums: [int], k: int) -> float:
        max_aver = None
        left = None
        for index in range(len(nums) - k + 1):
            if max_aver != None:
                aver = aver - left + nums[index + k - 1]
                if max_aver < aver:
                    max_aver = aver
            else:
                aver = sum(nums[index: index + k])
                max_aver = aver
            left = nums[index]
        return max_aver / k
