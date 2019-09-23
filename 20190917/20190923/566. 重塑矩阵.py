'''
Description: 重塑矩阵
Author: AskeyNil
CreateDate: 2019-09-23 09:53:50
LastEditors: AskeyNil

*********************************
**                             **
**     　  你只有足够努力     　  **
**       才能看上去毫不费力       **
**                             **
*********************************

'''


class Solution:
    def matrixReshape(self, nums: [[int]], r: int, c: int) -> [[int]]:
        # 限制条件 特判
        current_r = len(nums)
        if current_r == 0:
            return nums
        current_c = len(nums[0])
        if current_c == 0:
            return nums
        if current_c * current_r != r * c:
            return nums
        return [[nums[((x*c)+y) // current_c][((x*c)+y) % current_c] for y in range(c)] for x in range(r)]


print(Solution().matrixReshape([[1, 2, 3, 4]], 2, 2))
