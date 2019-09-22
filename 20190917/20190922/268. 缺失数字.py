'''
Description: 缺失数字
Author: AskeyNil
CreateDate: 2019-09-22 07:30:36
LastEditors: AskeyNil

*********************************
**                             **
**     　  你只有足够努力     　  **
**       才能看上去毫不费力       **
**                             **
*********************************

'''

# 排序法
# class Solution:
#     def missingNumber(self, nums: [int]) -> int:
#         nums.sort()
#         for index, num in enumerate(nums):
#             if index != num:
#                 return index
#         return len(nums)


# 求和法
class Solution:
    def missingNumber(self, nums: [int]) -> int:
        sum_number = sum(nums)
        length = len(nums)
        sum_number1 = (length + 1) * length // 2
        return sum_number1 - sum_number


print(Solution().missingNumber([0, 1, 2, 3, 4]))
