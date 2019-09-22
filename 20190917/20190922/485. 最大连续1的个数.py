'''
Description: 最大连续1的个数
Author: AskeyNil
CreateDate: 2019-09-22 20:14:25
LastEditors: AskeyNil

*********************************
**                             **
**     　  你只有足够努力     　  **
**       才能看上去毫不费力       **
**                             **
*********************************

'''


class Solution:
    def findMaxConsecutiveOnes(self, nums: [int]) -> int:
        max_length = 0
        current_length = 0
        for num in nums:
            if num == 0:
                if max_length < current_length:
                    max_length = current_length
                current_length = 0
            else:
                current_length += 1
        if max_length < current_length:
            max_length = current_length
        return max_length
