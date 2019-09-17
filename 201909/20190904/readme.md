# 18. 四数之和

## [题目](https://leetcode-cn.com/problems/4sum/)

给定一个包含 n 个整数的数组 `nums` 和一个目标值 `target`，判断 `nums` 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 `target` 相等？找出所有满足条件且不重复的四元组。

**注意**：

答案中不可以包含重复的四元组。

**示例**：

> 给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。
>
> 满足要求的四元组集合为：
>
> ```
> [
>   [-1,  0, 0, 1],
>   [-2, -1, 1, 2],
>   [-2,  0, 0, 2]
> ]
> ```

## [Python](./18.%20四数之和.py)

``` python
class Solution:
    def fourSum(self, nums: [int], target: int) -> [[int]]:
        len_nums = len(nums)
        i = 0
        nums.sort()
        temp_nums = []
        for i in range(len_nums - 3):
            # 去重
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, len_nums - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                k, l = j + 1, len_nums - 1
                while True:
                    temp = nums[i] + nums[j] + nums[k] + nums[l] - target

                    if temp == 0:
                        # 找到一个 跳出循环
                        temp_nums.append((nums[i], nums[j], nums[k], nums[l]))
                    if temp <= 0:
                        k += 1
                    else:
                        l -= 1
                    if k == l:
                        break
        return set(temp_nums)
```

