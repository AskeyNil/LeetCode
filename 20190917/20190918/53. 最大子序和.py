'''
Description: 最大子序和
Author: AskeyNil
CreateDate: 2019-09-18 07:38:32
LastEditors: AskeyNil

*********************************
**                             **
**     　  你只有足够努力     　  **
**       才能看上去毫不费力       **
**                             **
*********************************

'''


class Solution:
    def maxSubArray(self, nums: [int]) -> int:
        length = len(nums)
        if length == 0:
            return 0
        max_num = nums[0]
        left_max = nums[0]
        for num in nums[1:]:
            if left_max + num < num:
                left_max = num
            else:
                left_max += num
            if left_max > max_num:
                max_num = left_max
        return max_num


print(Solution().maxSubArray([1, 2, 3, 4]))
