'''
Description: 存在重复元素 II
Author: AskeyNil
CreateDate: 2019-09-21 22:33:03
LastEditors: AskeyNil

*********************************
**                             **
**     　  你只有足够努力     　  **
**       才能看上去毫不费力       **
**                             **
*********************************

'''


# 哈希法
class Solution:
    def containsNearbyDuplicate(self, nums: [int], k: int) -> bool:
        dic = {}
        for index, num in enumerate(nums):
            if num in dic:
                if index - dic[num] <= k:
                    return True
                else:
                    dic[num] = index
            else:
                dic[num] = index
        return False
