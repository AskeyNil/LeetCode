'''
Description: 按奇偶排序数组
Author: AskeyNil
CreateDate: 2019-09-26 09:48:35
LastEditors: AskeyNil

*********************************
**                             **
**     　  你只有足够努力     　  **
**       才能看上去毫不费力       **
**                             **
*********************************

'''


# 双指针
class Solution:
    def sortArrayByParity(self, A: [int]) -> [int]:
        left = 0
        right = len(A) - 1
        while left < right:
            is_left = A[left] % 2 == 0
            is_right = A[right] % 2 == 0
            if is_left and is_right:  # 左右都是偶数
                left += 1
            elif is_left and not is_right:  # 左边是偶数 右边是奇数
                left += 1
                right -= 1
            elif not is_left and is_right:  # 左边是奇数 右边是偶数
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1
            else:
                right -= 1
        return A
