# 674. 最长连续递增序列

## [题目](https://leetcode-cn.com/problems/longest-continuous-increasing-subsequence/)

给定一个未经排序的整数数组，找到最长且连续的的递增序列。

示例 1:

> 输入: [1,3,5,4,7]
>
> 输出: 3
>
> 解释: 最长连续递增序列是 [1,3,5], 长度为3。
>
> 尽管 [1,3,5,7] 也是升序的子序列, 但它不是连续的，因为5和7在原数组里被4隔开。 

示例 2:

> 输入: [2,2,2,2,2]
>
> 输出: 1
>
> 解释: 最长连续递增序列是 [2], 长度为1。

**注意**：数组长度不会超过10000。



## [Python](./674.%20最长连续递增序列.py)

```python
class Solution:
    def findLengthOfLCIS(self, nums: [int]) -> int:
        if len(nums) == 0:
            return 0
        max_count = 0
        count = 1
        left = None
        for num in nums:
            if left != None:
                if num > left:
                    count += 1
                else:
                    if max_count < count:
                        max_count = count
                    count = 1
            left = num
        return max(max_count, count)
```



## [C++](./674.%20最长连续递增序列.cc)

```c++
class Solution {
  public:
    int findLengthOfLCIS(vector<int> &nums) {
        if (nums.empty())
            return 0;
        int max_count = 0, count = 1, *left = nullptr;
        for (int &num : nums) {
            if (left != nullptr) {
                if (num > *left)
                    count += 1;
                else {
                    if (max_count < count)
                        max_count = count;
                    count = 1;
                }
            }
            left = &num;
        }
        return max_count > count ? max_count : count;
    }
};
```

# 697. 数组的度

## [题目](https://leetcode-cn.com/problems/degree-of-an-array/)

## [Python](./697.%20数组的度.py)

```python
class Solution:
    def findShortestSubArray(self, nums: [int]) -> int:
        if len(nums) == 0:
            return 0
        dic = {}
        for index, num in enumerate(nums):
            if num in dic:
                dic[num][0] += 1
                dic[num][2] = index
            else:
                dic[num] = [1, index, index]
        re_count = 0
        max_number = None
        for number, start, end in dic.values():
            if max_number == None:
                max_number = number
                re_count = end - start + 1
            else:
                if number > max_number:
                    max_number = number
                    re_count = end - start + 1
                if number == max_number:
                    count = end - start + 1
                    if count < re_count:
                        re_count = count
        return re_count
```



## [C++](./697.%20数组的度.cc)

```c++
class Solution {
  public:
    int findShortestSubArray(vector<int> &nums) {
        if (nums.empty())
            return 0;
        map<int, vector<int>> dic;
        for (int i = 0; i < nums.size(); i++) {
            if (dic.count(nums[i]) == 0)
                dic[nums[i]] = vector<int>{1, i, i};
            else
                dic[nums[i]][0] += 1, dic[nums[i]][2] = i;
        }

        int re_count = 0, *max_number = nullptr;
        for (auto v : dic) {
            if (max_number == nullptr) {
                max_number = new int(v.second[0]);
                re_count = v.second[2] - v.second[1] + 1;
            } else {
                if (v.second[0] > *max_number) {
                    *max_number = v.second[0];
                    re_count = v.second[2] - v.second[1] + 1;
                } else if (v.second[0] == *max_number) {
                    int count = v.second[2] - v.second[1] + 1;
                    if (count < re_count) {
                        re_count = count;
                    }
                }
            }
        }
        return re_count;
    }
};
```

