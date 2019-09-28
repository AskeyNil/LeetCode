'''
Description: 有序数组的平方
Author: AskeyNil
CreateDate: 2019-09-28 08:31:03
LastEditors: AskeyNil

*********************************
**                             **
**     　  你只有足够努力     　  **
**       才能看上去毫不费力       **
**                             **
*********************************

'''


# class Solution:
#     def sortedSquares(self, A: [int]) -> [int]:
#         for index, num in enumerate(A):
#             A[index] = num * num
#         A.sort()
#         return A

# Python 特有一行法
# class Solution:
#     def sortedSquares(self, A: [int]) -> [int]:
#         return sorted([num * num for num in A])


# 双指针
class Solution:
    def sortedSquares(self, A: [int]) -> [int]:
        left = 0, A[0] ** 2
        right = len(A) - 1, A[len(A) - 1] ** 2
        B = [0 for _ in range(len(A))]
        index = right[0]
        while index >= 0:
            if left[1] < right[1]:
                B[index] = right[1]
                if right[0] != 0:
                    right = right[0] - 1, A[right[0] - 1] ** 2
            else:
                B[index] = left[1]
                if left[0] + 1 != len(A):
                    left = left[0] + 1, A[left[0] + 1] ** 2
            index -= 1
        return B
