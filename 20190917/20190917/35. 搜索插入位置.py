'''
Description: 搜索插入位置
Author: AskeyNil
CreateDate: 2019-09-17 20:38:54
LastEditors: AskeyNil

*********************************
**                             **
**     　  你只有足够努力     　  **
**       才能看上去毫不费力       **
**                             **
*********************************

'''


# 暴力遍历
# class Solution:
#     def searchInsert(self, nums: [int], target: int) -> int:
#         for index, num in enumerate(nums):
#             if num >= target:
#                 return index
#         return len(nums)


# 二分查找
class Solution:
    def searchInsert(self, nums: [int], target: int) -> int:
        length = len(nums)
        if length == 0:
            return 0
        left = 0
        right = length
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left


print(Solution().searchInsert([1, 3, 5, 6], 7))
