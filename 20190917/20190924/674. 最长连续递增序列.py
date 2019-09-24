'''
Description: 最长连续递增序列
Author: AskeyNil
CreateDate: 2019-09-24 09:13:33
LastEditors: AskeyNil

*********************************
**                             **
**     　  你只有足够努力     　  **
**       才能看上去毫不费力       **
**                             **
*********************************

'''


class Solution:
    def findLengthOfLCIS(self, nums: [int]) -> int:
        if len(nums) == 0:
            return 0
        max_count = 0
        count = 1
        left = None
        for num in nums:
            if left != None:
                if num > left:
                    count += 1
                else:
                    if max_count < count:
                        max_count = count
                    count = 1
            left = num
        return max(max_count, count)
