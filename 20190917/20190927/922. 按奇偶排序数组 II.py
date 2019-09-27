'''
Description: 按奇偶排序数组 II
Author: AskeyNil
CreateDate: 2019-09-27 18:19:05
LastEditors: AskeyNil

*********************************
**                             **
**     　  你只有足够努力     　  **
**       才能看上去毫不费力       **
**                             **
*********************************

'''


# # 沙雕思路
# class Solution:
#     def sortArrayByParityII(self, A: [int]) -> [int]:
#         left = []
#         for index, num in enumerate(A):
#             if (num - index) % 2 != 0:
#                 if not left:
#                     left.append(index)
#                 else:
#                     if (num - A[left[-1]]) % 2 == 0:
#                         left.append(index)
#                     else:
#                         A[index], A[left[-1]] = A[left[-1]], A[index]
#                         left.pop()
#         return A


# 双指针
class Solution:
    def sortArrayByParityII(self, A: [int]) -> [int]:
        odd = 1
        even = 0
        length = len(A)
        while odd < length and even < length:
            print(odd, even)
            is_odd = (A[odd] - odd) % 2
            is_even = (A[even] - even) % 2
            if is_odd == 1 and is_even == 1:
                A[even], A[odd] = A[odd], A[even]
            if is_odd == is_even:
                odd += 2
                even += 2
            elif is_odd == 0:
                odd += 2
            elif is_even == 0:
                even += 2
        return A


print(Solution().sortArrayByParityII(
    [648, 831, 560, 986, 192, 424, 997, 829, 897, 843]))
