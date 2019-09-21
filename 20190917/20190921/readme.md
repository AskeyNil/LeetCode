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



# 122. 买卖股票的最佳时机 II

## [题目](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/)

给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

**示例** 1:

> **输入**: [7,1,5,3,6,4]
>
> **输出**: 7
>
> **解释**: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。 随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。

**示例** 2:

> **输入**: [1,2,3,4,5]
>
> **输出**: 4
>
> **解释**: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
>
> 注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。
>
> 因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。

**示例** 3:

> **输入**: [7,6,4,3,1]
>
> **输出**: 0
>
> **解释**: 在这种情况下, 没有交易完成, 所以最大利润为 0。

## [Python](./122.%20买卖股票的最佳时机%20II.py)

``` python
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
```

## [C++](./122.%20买卖股票的最佳时机%20II.cc)

``` c++
class Solution {
   public:
    int maxProfit(vector<int>& prices) {
        int length = prices.size();
        if (length <= 1) return 0;
        int sum = 0, left = prices[0];
        for (auto i = 1; i < length; i++) {
            if (prices[i] > left) sum += prices[i] - left;
            left = prices[i];
        }
        return sum;
    }
};
```

