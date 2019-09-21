'''
Description: 两数之和 II - 输入有序数组
Author: AskeyNil
CreateDate: 2019-09-21 20:02:29
LastEditors: AskeyNil

*********************************
**                             **
**     　  你只有足够努力     　  **
**       才能看上去毫不费力       **
**                             **
*********************************

'''


# 哈希表
class Solution:
    def twoSum(self, numbers: [int], target: int) -> [int]:
        dic = {}
        for index, number in enumerate(numbers):
            dif = target - number
            if dif in dic:
                return [dic[dif] + 1, index + 1]
            dic[number] = index


print(Solution().twoSum([2, 7, 11, 15], 17))
