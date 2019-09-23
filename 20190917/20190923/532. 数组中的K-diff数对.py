'''
Description: 数组中的K-diff数对
Author: AskeyNil
CreateDate: 2019-09-23 08:22:17
LastEditors: AskeyNil

*********************************
**                             **
**     　  你只有足够努力     　  **
**       才能看上去毫不费力       **
**                             **
*********************************

'''


# 两张哈希表
class Solution:
    def findPairs(self, nums: [int], k: int) -> int:
        dic = {}
        temp = set()
        for num in nums:
            # 分两种情况
            # 1. 假设 num >= prev
            prev = num - k
            if prev in dic:
                if num >= prev:
                    temp.add((num, prev))
                    continue
            # 2. 假设 num <= prev
            prev = k + num
            if prev in dic:
                if num <= prev:
                    temp.add((prev, num))
            dic[num] = 0
        return len(temp)


print(Solution().findPairs([1, 3, 1, 5, 4], 0))
