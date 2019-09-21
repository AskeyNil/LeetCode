# 121. 买卖股票的最佳时机

## [题目](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/)

## [Python](./121.%20买卖股票的最佳时机.py)

### 动态规划

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

### 动态规划

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



## 思路

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



# 167. 两数之和 II - 输入有序数组

## [题目](https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/)

## [Python](./167.%20两数之和%20II%20-%20输入有序数组.py)

### 哈希表

``` python
class Solution:
    def twoSum(self, numbers: [int], target: int) -> [int]:
        dic = {}
        for index, number in enumerate(numbers):
            dif = target - number
            if dif in dic:
                return [dic[dif] + 1, index + 1]
            dic[number] = index

```



## [C++](./167.%20两数之和%20II%20-%20输入有序数组.cc)

### 双指针

``` c++
class Solution {
   public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int pre = 0, tail = numbers.size() - 1;
        while (pre < tail) {
            if (numbers[pre] + numbers[tail] == target) {
                return {pre + 1, tail + 1};
            } else if (numbers[pre] + numbers[tail] > target) {
                tail -= 1;
            } else {
                pre += 1;
            }
        }
        return {};
    }
};
```

# 169. 求众数

## [题目](https://leetcode-cn.com/problems/majority-element/)

给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在众数。

示例 1:

> 输入: [3,2,3]
>
> 输出: 3

示例 2:

> 输入: [2,2,1,1,1,2,2]
>
> 输出: 2



## [Python](./169.%20求众数.py)

### 一次哈希表

```python
class Solution:
    def majorityElement(self, nums: [int]) -> int:
        length = len(nums)
        if length == 1:
            return nums[0]
        dic = {}
        for num in nums:
            if num in dic:
                dic[num] += 1
                if dic[num] > length / 2:
                    return num
            else:
                dic[num] = 1
```

### 排序法

```python
class Solution:
    def majorityElement(self, nums: [int]) -> int:
        return sorted(nums)[len(nums) // 2]
```

### *Boyer-Moore 投票算法*

```python
class Solution:
    def majorityElement(self, nums: [int]) -> int:
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else - 1
        return candidate
```



## [C++](./169.%20求众数.cc)

### 一次哈希表

```c++
class Solution {
   public:
    int majorityElement(vector<int>& nums) {
        map<int, int> dic;
        int length = nums.size();
        for (auto num : nums) {
            if (dic.count(num) == 0) {
                dic[num] = 1;
            } else {
                dic[num] += 1;
            }
            if (dic[num] > length / 2.0) return num;
        }
        return nums[0];
    }
};
```

### Boyer-Moore 投票算法

```c++
class Solution {
   public:
    int majorityElement(vector<int>& nums) {
        int count = 0, candidate = nums[0];
        for (auto num : nums) {
            if (count == 0) candidate = num;
            count += num == candidate ? 1 : -1;
        }
        return candidate;
    }
};
```

## 总结

### [Boyer-Moore 投票算法](https://leetcode-cn.com/problems/majority-element/solution/qiu-zhong-shu-by-leetcode-2/)

根据众数的特性，一定要多于数组中的一半的元素，那么如果众数为+1，其他为-1，则最终结果一定会大于 0，若为 0 则不是众数，不断排除，即可得到众数

> 例子：
>
> ` [7, 7, 5, 7, 5, 1 | 5, 7 | 5, 5, 7, 7 | 7, 7, 7, 7]`
>
> 1. 从左边往右边开始遍历，遇到 7，我们将其假设为众数，
> 2. 当遍历到`|`位置的时候，此时 count 为 0，我们将后面的 5 再次假设为众数
> 3. 继续往后遍历，当 count 为 0时，便重新将下一个数设置为众数。
> 4. 直到最后遍历出 7 为众数，此时 count > 0
> 5. 因为众数的规则，最后总有 count > 0。

# 189. 旋转数组

## [题目](https://leetcode-cn.com/problems/rotate-array/)

## [Python](./189.%20旋转数组.cc)

### 插入法

```python
class Solution:
    def rotate(self, nums: [int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for _ in range(k):
            n = nums.pop()
            nums.insert(0, n)
```

### 切片法

```python
class Solution:
    def rotate(self, nums: [int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]
```



## [C++](./189.%20旋转数组.cc)

### 插入法

```c++
class Solution {
   public:
    void rotate(vector<int>& nums, int k) {
        k %= nums.size();
        for (int i = 0; i < k; i++) {
            int temp = nums[nums.size() - 1];
            nums.pop_back();
            nums.insert(nums.begin(), temp);
        }
    }
};
```

### 三次翻转

```C++
class Solution {
   public:
    void rotate(vector<int>& nums, int k) {
        k %= nums.size();
        // 全部翻转
        reverse(nums.begin(), nums.end());
        // 翻转前 k 个
        reverse(nums.begin(), nums.begin() + k);
        // 翻转剩余的
        reverse(nums.begin() + k, nums.end());
    }
};
```

# 217. 存在重复元素

## [题目](https://leetcode-cn.com/problems/contains-duplicate/)

## [Python](./217.%20存在重复元素.py)

### 暴力法

```python
class Solution:
    def containsDuplicate(self, nums: [int]) -> bool:
        return len(set(nums)) < len(nums)
      
```

### 哈希法

```python
class Solution:
    def containsDuplicate(self, nums: [int]) -> bool:
        dic = {}
        for num in nums:
            if num in dic:
                return True
            else:
                dic[num] = 0
        return False
```

### 排序法

```python
class Solution:
    def containsDuplicate(self, nums: [int]) -> bool:
        nums.sort()
        for index in range(len(nums) - 1):
            if nums[index] == nums[index + 1]:
                return True
        return False
```



## [C++](./217.%20存在重复元素.cc)

### 哈希法

```c++
class Solution {
   public:
    bool containsDuplicate(vector<int>& nums) {
        map<int, int> dic;
        for (int num : nums) {
            if (dic.count(num) == 0)
                dic[num] = 0;
            else
                return true;
        }
        return false;
    }
};
```

### 排序法

```c++
class Solution {
   public:
    bool containsDuplicate(vector<int>& nums) {
        if (nums.empty()) return false;
        sort(nums.begin(), nums.end());
        for (auto i = 0; i < nums.size() - 1; i++) {
            if (nums[i] == nums[i + 1]) return true;
        }
        return false;
    }
};
```



# 219. 存在重复元素 II

## [题目](https://leetcode-cn.com/problems/contains-duplicate-ii/)

给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的绝对值最大为 k。

**示例** 1:

> 输入: nums = [1,2,3,1], k = 3
>
> 输出: true

**示例** 2:

> 输入: nums = [1,0,1,1], k = 1
>
> 输出: true

**示例** 3:

> 输入: nums = [1,2,3,1,2,3], k = 2
>
> 输出: false

## [Python](./219.%20存在重复元素%20II.py)

### 哈希法

```python
class Solution:
    def containsNearbyDuplicate(self, nums: [int], k: int) -> bool:
        dic = {}
        for index, num in enumerate(nums):
            if num in dic:
                if index - dic[num] <= k:
                    return True
                else:
                    dic[num] = index
            else:
                dic[num] = index
        return False
```



## [C++](./219.%20存在重复元素%20II.py)

### 哈希法

```c++
class Solution {
   public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        map<int, int> dic;
        for (int i = 0; i < nums.size(); i++) {
            if (dic.count(nums[i]) == 0) {
                dic[nums[i]] = i;
            } else {
                if (i - dic[nums[i]] <= k) return true;
                dic[nums[i]] = i;
            }
        }
        return false;
    }
};
```

