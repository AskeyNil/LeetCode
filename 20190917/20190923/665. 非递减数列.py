'''
Description: 非递减数列
Author: AskeyNil
CreateDate: 2019-09-23 15:24:02
LastEditors: AskeyNil

*********************************
**                             **
**     　  你只有足够努力     　  **
**       才能看上去毫不费力       **
**                             **
*********************************

'''


# 特判
class Solution:
    def checkPossibility(self, nums: [int]) -> bool:
        p = None
        for index in range(len(nums) - 1):
            if nums[index] > nums[index + 1]:
                if p is not None:
                    return False
                p = i
        return (p is None or p == 0 or p == len(nums) - 2 or nums[p-1] <= A[P+1] or nums[p] <= nums[p+2])
