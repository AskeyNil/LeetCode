'''
Description: 数组形式的整数加法
Author: AskeyNil
CreateDate: 2019-09-28 18:52:46
LastEditors: AskeyNil

*********************************
**                             **
**     　  你只有足够努力     　  **
**       才能看上去毫不费力       **
**                             **
*********************************

'''


class Solution:
    def addToArrayForm(self, A: [int], K: int) -> [int]:
        return list(str(int("".join([str(num) for num in A])) + K))


print(Solution().addToArrayForm([1, 2, 0, 0], 34))
