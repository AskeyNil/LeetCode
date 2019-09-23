'''
Description: 最短无序连续子数组
Author: AskeyNil
CreateDate: 2019-09-23 10:25:52
LastEditors: AskeyNil

*********************************
**                             **
**     　  你只有足够努力     　  **
**       才能看上去毫不费力       **
**                             **
*********************************

'''


# 排序
class Solution:
    def findUnsortedSubarray(self, nums: [int]) -> int:
        sorted_nums = sorted(nums)
        start = None
        end = None
        for index, num in enumerate(nums):
            if start == None and num != sorted_nums[index]:
                start = index
            elif end == None and num == sorted_nums[index]:
                end = index
            elif end != None and num != sorted_nums[index]:
                end = index
        if end == None:
            end = len(nums) - 1
        return end - start + 1
