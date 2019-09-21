'''
Description: 存在重复元素
Author: AskeyNil
CreateDate: 2019-09-21 22:11:21
LastEditors: AskeyNil

*********************************
**                             **
**     　  你只有足够努力     　  **
**       才能看上去毫不费力       **
**                             **
*********************************

'''

# 暴力法
# class Solution:
#     def containsDuplicate(self, nums: [int]) -> bool:
#         return len(set(nums)) < len(nums)

# 哈希表
# class Solution:
#     def containsDuplicate(self, nums: [int]) -> bool:
#         dic = {}
#         for num in nums:
#             if num in dic:
#                 return True
#             else:
#                 dic[num] = 0
#         return False


# 排序法
class Solution:
    def containsDuplicate(self, nums: [int]) -> bool:
        nums.sort()
        for index in range(len(nums) - 1):
            if nums[index] == nums[index + 1]:
                return True
        return False
