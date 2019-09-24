'''
Description: 使用最小花费爬楼梯
Author: AskeyNil
CreateDate: 2019-09-24 12:05:46
LastEditors: AskeyNil

*********************************
**                             **
**     　  你只有足够努力     　  **
**       才能看上去毫不费力       **
**                             **
*********************************

'''


# 动态规划
class Solution:
    def minCostClimbingStairs(self, cost: [int]) -> int:
        length = len(cost)
        dp = [cost[0], cost[1]]
        for index in range(2, length):
            print(dp)
            dp.append(min(dp[index - 2], dp[index - 1]) + cost[index])
        return min(dp[-1], dp[-2])


Solution().minCostClimbingStairs([0, 1, 2, 2])
