# 121. 买卖股票的最佳时机

## [题目](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/)

## [Python](./121.%20买卖股票的最佳时机.py)

#### 动态规划

从左往右规划

``` python
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
```

从右往左规划

``` python
class Solution:
    def maxProfit(self, prices: [int]) -> int:
        length = len(prices)
        if length == 0 or length == 1:
            return 0
        large = prices[-1]
        diff = 0
        for index in range(length - 2, -1, -1):
            temp = large - prices[index]
            if temp > diff:
                diff = temp
            elif temp < 0:
                large = prices[index]
        return diff
```



## [C++](./121.%20买卖股票的最佳时机.cc)

#### 动态规划

``` c++
class Solution {
   public:
    int maxProfit(vector<int>& prices) {
        int length = prices.size();
        if (length == 0 || length == 1) {
            return 0;
        }
        int diff = 0, mini = prices[0];
        for (int i = 0; i < length; i++) {
            int temp = prices[i] - mini;
            if (temp > diff)
                diff = temp;
            else if (temp < 0)
                mini = prices[i];
        }
        return diff;
    }
};
```



### 思路

> 用原题的数组举例，从左到右遍历一遍，时间复杂度 o(n)
>
> `[7,1,5,3,6,4]`
>
> 先将数组中的第一个元素保存下来，从第二个元素开始遍历
>
> 1. 当 `i=1`时，卖出价格为 `1`,此时只有一种情况，买入`7`，卖出 `1`，净亏`6`，显然不符合，此时最低的买入价为 `1`
>
> 2. 当`i=2`时，卖出价格为 `5`，之前的最低买入价为`1`，净赚 `4`，保存最大的净赚数字，以便返回
> 3. 以此类推。。。



