# 16. 最接近的三数之和
## [题目](https://leetcode-cn.com/problems/3sum-closest/)

给定一个包括 n 个整数的数组 `nums` 和 一个目标值 `target`。找出 `nums` 中的三个整数，使得它们的和与 `target` 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

> 例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
>
> 与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
>

## [Python](./16.%20最接近的三数之和.py)

``` python
class Solution:
    def threeSumClosest(self, nums: [int], target: int) -> int:
        nums.sort()
        len_nums = len(nums)
        k = 0
        dif = 999999
        result_num = 0
        for k in range(0, len_nums-2):
            i, j = k + 1, len_nums - 1
            if k > 0 and nums[k] == nums[k - 1]:
                continue
            while i < j:
                num = nums[i] + nums[j] + nums[k]
                temp_dif = num - target
                if abs(temp_dif) < dif:
                    print(temp_dif)
                    dif = abs(temp_dif)
                    result_num = num
                if temp_dif < 0:
                    i += 1
                elif temp_dif > 0:
                    j -= 1
                else:
                    return result_num
        return result_num
```
