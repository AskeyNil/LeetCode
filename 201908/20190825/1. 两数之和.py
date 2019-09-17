'''
Description: 两数之和
Author: AskeyNil
CreateDate: 2019-08-25 20:03:28
LastEditors: AskeyNil

********************************
**                            **
**   It works on my machine   **
**                            **
********************************
'''

"""
'     给定一个整数数组 nums 和一个目标值 target，
' 请你在该数组中找出和为目标值的那两个整数，并返回
' 他们的数组下标。你可以假设每种输入只会对应一个答
' 案。但是，你不能重复利用这个数组中同样的元素。
'
' 示例:
'     给定 nums = [2, 7, 11, 15], target = 9
'     因为 nums[0] + nums[1] = 2 + 7 = 9
'     所以返回 [0, 1]
"""

# ! ######################   START   ##########################


class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        dic = {}
        for index, num in enumerate(nums):
            if target - num in dic:
                return [dic[target - num], index]
            else:
                dic[num] = index


print(Solution().twoSum([2, 7, 11, 15], 9))
