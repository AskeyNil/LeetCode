'''
Description: 旋转数组
Author: AskeyNil
CreateDate: 2019-09-21 21:32:44
LastEditors: AskeyNil

*********************************
**                             **
**     　  你只有足够努力     　  **
**       才能看上去毫不费力       **
**                             **
*********************************

'''


# 插入法
# class Solution:
#     def rotate(self, nums: [int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         for _ in range(k):
#             n = nums.pop()
#             nums.insert(0, n)

# 切片法
# class Solution:
#     def rotate(self, nums: [int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         k %= len(nums)
#         nums[:] = nums[-k:] + nums[:-k]
