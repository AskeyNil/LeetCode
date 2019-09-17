'''
Description: 移除元素
Author: AskeyNil
CreateDate: 2019-09-17 20:00:19
LastEditors: AskeyNil

*********************************
**                             **
**     　  你只有足够努力     　  **
**       才能看上去毫不费力       **
**                             **
*********************************

'''


class Solution:
    def removeElement(self, nums: [int], val: int) -> int:
        i = 0
        for (index, num) in enumerate(nums):
            if nums[index] != val:
                nums[i] = nums[index]
                i += 1
        return i


a = [0, 1, 2, 2, 3, 0, 4, 2]
print(Solution().removeElement(a, 2))
print(a)
