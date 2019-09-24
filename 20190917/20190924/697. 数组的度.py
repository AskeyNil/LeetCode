'''
Description: 数组的度
Author: AskeyNil
CreateDate: 2019-09-24 09:38:11
LastEditors: AskeyNil

*********************************
**                             **
**     　  你只有足够努力     　  **
**       才能看上去毫不费力       **
**                             **
*********************************

'''


class Solution:
    def findShortestSubArray(self, nums: [int]) -> int:
        if len(nums) == 0:
            return 0
        dic = {}
        for index, num in enumerate(nums):
            if num in dic:
                dic[num][0] += 1
                dic[num][2] = index
            else:
                dic[num] = [1, index, index]
        re_count = 0
        max_number = None
        for number, start, end in dic.values():
            if max_number == None:
                max_number = number
                re_count = end - start + 1
            else:
                if number > max_number:
                    max_number = number
                    re_count = end - start + 1
                if number == max_number:
                    count = end - start + 1
                    if count < re_count:
                        re_count = count
        return re_count
