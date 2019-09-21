'''
Description: 买卖股票的最佳时机 II
Author: AskeyNil
CreateDate: 2019-09-21 19:41:31
LastEditors: AskeyNil

*********************************
**                             **
**     　  你只有足够努力     　  **
**       才能看上去毫不费力       **
**                             **
*********************************

'''


class Solution:
    def maxProfit(self, prices: [int]) -> int:
        length = len(prices)
        if length <= 1:
            return 0
        sum_price = 0
        left = prices[0]
        for index in range(1, length):
            if prices[index] > left:
                sum_price += prices[index] - left
            left = prices[index]
        return sum_price


print(Solution().maxProfit([7, 6, 4, 3, 1]))
