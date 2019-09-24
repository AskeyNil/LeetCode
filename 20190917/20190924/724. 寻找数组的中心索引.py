'''
Description: 寻找数组的中心索引
Author: AskeyNil
CreateDate: 2019-09-24 11:32:18
LastEditors: AskeyNil

*********************************
**                             **
**     　  你只有足够努力     　  **
**       才能看上去毫不费力       **
**                             **
*********************************

'''


class Solution:
    def pivotIndex(self, nums: [int]) -> int:
        length = len(nums)
        left = None
        right = None
        for index in range(length):
            if left == None:
                left = sum(nums[0:index])
                right = sum(nums[index+1:])
            else:
                left += nums[index-1]
                right -= nums[index]
            if left == right:
                return index + 1
        return -1
