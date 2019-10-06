'''
Description: 步进数
Author: AskeyNil
CreateDate: 2019-10-05 23:01:28
LastEditors: AskeyNil

*********************************
**                             **
**     　  你只有足够努力     　  **
**       才能看上去毫不费力       **
**                             **
*********************************

'''


class Solution:
    def countSteppingNumbers(self, low: int, high: int) -> [int]:
        result = set()
        for number in range(low, high + 1):
            n = number // 10
            if n == 0:
                result.add(number)
            else:
                if n in result:
                    bits = number % 10
                    ten = n % 10
                    if abs(ten - bits) == 1:
                        result.add(number)
        return sorted(list(result))


print(Solution().countSteppingNumbers(0, 1000000000))
