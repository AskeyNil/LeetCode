'''
Description: 移动零
Author: AskeyNil
CreateDate: 2019-09-22 18:08:32
LastEditors: AskeyNil

*********************************
**                             **
**     　  你只有足够努力     　  **
**       才能看上去毫不费力       **
**                             **
*********************************

'''

# 查找元素 删除 放到最后去
# class Solution:
#     def moveZeroes(self, nums: [int]):
#         count = len(nums)
#         index = 0
#         while index < count:
#             if nums[index] == 0:
#                 nums.pop(index)
#                 nums.add(0)
#                 count -= 1
#             else:
#                 index += 1


# 双指针
# class Solution:
#     def moveZeroes(self, nums: [int]):
#         left = 0
#         right = 0
#         length = len(nums)
#         while right < length:
#             if nums[right] != 0:
#                 nums[left] = nums[right]
#                 left += 1
#             right += 1
#         nums[left:right] = [0 for _ in range(right - left)]
