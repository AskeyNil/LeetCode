'''
Description: 斐波那契数
Author: AskeyNil
CreateDate: 2019-09-23 07:49:14
LastEditors: AskeyNil

*********************************
**                             **
**     　  你只有足够努力     　  **
**       才能看上去毫不费力       **
**                             **
*********************************

'''


# 递归
# class Solution:
#     def fib(self, N: int) -> int:
#         if N == 0:
#             return 0
#         elif N == 1:
#             return 1
#         else:
#             return self.fib(N-1) + self.fib(N-2)


# 动态规划
class Solution:
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        else if N == 1 or N == 2:
            return 1
        current = 1
        previous = 1
        for index in range(3, N+1):
            current = current + previous
            previous = current - previous
        return current
