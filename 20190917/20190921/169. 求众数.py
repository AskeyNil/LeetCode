'''
Description: 求众数
Author: AskeyNil
CreateDate: 2019-09-21 20:42:25
LastEditors: AskeyNil

*********************************
**                             **
**     　  你只有足够努力     　  **
**       才能看上去毫不费力       **
**                             **
*********************************

'''


# 一次哈希表
# class Solution:
#     def majorityElement(self, nums: [int]) -> int:
#         length = len(nums)
#         if length == 1:
#             return nums[0]
#         dic = {}
#         for num in nums:
#             if num in dic:
#                 dic[num] += 1
#                 if dic[num] > length / 2:
#                     return num
#             else:
#                 dic[num] = 1


# 排序法
# class Solution:
#     def majorityElement(self, nums: [int]) -> int:
#         return sorted(nums)[len(nums) // 2]


# Boyer-Moore 投票算法
class Solution:
    def majorityElement(self, nums: [int]) -> int:
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else - 1
        return candidate


print(Solution().majorityElement([4, 5, 4]))
