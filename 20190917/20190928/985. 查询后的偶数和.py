'''
Description: 查询后的偶数和
Author: AskeyNil
CreateDate: 2019-09-28 14:00:51
LastEditors: AskeyNil

*********************************
**                             **
**     　  你只有足够努力     　  **
**       才能看上去毫不费力       **
**                             **
*********************************

'''


class Solution:
    def sumEvenAfterQueries(self, A: [int], queries: [[int]]) -> [int]:
        sum_start = 0
        for num in A:
            if num % 2 == 0:
                sum_start += num
        result = []
        for val, index in queries:
            if A[index] % 2 == 0:
                sum_start -= A[index]
            A[index] += val
            if A[index] % 2 == 0:
                sum_start += A[index]
            result.append(sum_start)
        return result
