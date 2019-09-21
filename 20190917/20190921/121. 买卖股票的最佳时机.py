'''
Description: 买卖股票的最佳时机
Author: AskeyNil
CreateDate: 2019-09-21 07:42:46
LastEditors: AskeyNil

*********************************
**                             **
**     　  你只有足够努力     　  **
**       才能看上去毫不费力       **
**                             **
*********************************

'''

# 从后往前推
# class Solution:
#     def maxProfit(self, prices: [int]) -> int:
#         length = len(prices)
#         if length <= 1:
#             return 0
#         large = prices[-1]
#         diff = 0
#         for index in range(length - 2, -1, -1):
#             temp = large - prices[index]
#             if temp > diff:
#                 diff = temp
#             elif temp < 0:
#                 large = prices[index]
#         return diff


# 从前往后推
class Solution:
    def maxProfit(self, prices: [int]) -> int:
        length = len(prices)
        if length == 0 or length == 1:
            return 0
        mini = prices[0]
        diff = 0
        for index in range(1, length):
            temp = prices[index] - mini
            if temp > diff:
                diff = temp
            elif temp < 0:
                mini = prices[index]
        return diff


print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
