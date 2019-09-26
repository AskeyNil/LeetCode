'''
Description: 公平的糖果交换
Author: AskeyNil
CreateDate: 2019-09-26 08:45:30
LastEditors: AskeyNil

*********************************
**                             **
**     　  你只有足够努力     　  **
**       才能看上去毫不费力       **
**                             **
*********************************

'''


class Solution:
    def fairCandySwap(self, A: [int], B: [int]) -> [int]:
        sum_A = sum(A)
        sum_B = sum(B)
        A.sort()
        B.sort()
        diff = sum_A - sum_B
        index = 0
        for num in A:
            temp = num - diff // 2
            while True:
                if temp > B[index]:
                    index += 1
                    continue
                elif temp == B[index]:
                    return [num, temp]
                else:
                    break
        return [0, 0]

#  强行 set


class Solution:
    def fairCandySwap(self, A: [int], B: [int]) -> [int]:
        sum_A = sum(A)
        sum_B = sum(B)
        diff = sum_A - sum_B
        set_b = set(B)
        for num in A:
            temp = num - diff // 2
            if temp in set_b:
                return [num, temp]
        return [0, 0]
