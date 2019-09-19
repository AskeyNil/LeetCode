'''
Description: 合并两个有序数组
Author: AskeyNil
CreateDate: 2019-09-19 21:22:38
LastEditors: AskeyNil

*********************************
**                             **
**     　  你只有足够努力     　  **
**       才能看上去毫不费力       **
**                             **
*********************************

'''


class Solution:
    def merge(self, nums1: [int], m: int, nums2: [int], n: int) -> None:
        nums1[:] = sorted(nums1[:m] + nums2)


s = [1, 2, 3]
s2 = [2, 5, 6]
Solution().merge(s, 3, s2, 3)
print(s)
