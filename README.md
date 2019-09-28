# LeetCode

> 题目均来自 [LeetCode 中国官网](https://leetcode-cn.com)

> 题解 :
>
> 1. ✅ 解出
> 3. ⁉️ 未理解
> 
>难度：
> 
>1. ★        简单
> 2. ★★     中等
> 3. ★★★ 困难



> 2019.09.17 记
>
> 根据前段时间按顺序刷题的自我反馈与认识，感觉刷题过于混乱且无效率，做一些计划整理
>
> 按顺序做 `array` -> `string` -> `tree` -> `linkedlist` -> `math`
>
> 按难度做 `easy` -> `medium` -> `hard`
>
> 更好的归纳总结每日的算法
>
> 故 9 月特地新开一个文件夹，记录 9 月 17 日之后的学习记录
>
> 9 月 17 之前的 在之后回刷的时候，再次进行整理，总结
>
> 且开始用 Python 和 C++ 两种语言


## 2019.09.17

> 开始，[array and easy](https://leetcode-cn.com/problemset/all/?topicSlugs=array&difficulty=%E7%AE%80%E5%8D%95)
>
> 查询总个数 js `$(".reactable-data").children("tr").length`
>
> 查询已做个数`$(".text-success.fa.fa-check").length`
>
> 查询上锁个数`$(".fa.fa-lock").length-1`
>
> 未做的个数`$(".reactable-data").children("tr").length-$(".text-success.fa.fa-check").length-$(".fa.fa-lock").length+1`
>
> 截止 20190923 [array and easy](https://leetcode-cn.com/problemset/all/?topicSlugs=array&difficulty=%E7%AE%80%E5%8D%95)
>
> 1. 总数：72
> 2. 已做：46
> 3. 上锁：8
> 4. 剩余：18

| #    | 题目                                                         | 题解                                                         | 难度 | 时间       | tag                      |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ | ---- | ---------- | ------------------------ |
| 27   | [移动元素](https://leetcode-cn.com/problems/remove-element/) | [Python](./20190917/20190917/readme.md#Python)✅ [C++](./20190917/20190917/readme.md#C)✅ | ★    | 2019.09.17 |                          |
| 35   | [搜索插入位置](https://leetcode-cn.com/problems/search-insert-position/) | [Python](./20190917/20190917/readme.md#Python-1)✅ [C++](./20190917/20190917/readme.md#C-1)✅ | ★    | 2019.09.17 | 二分查找                 |
| 53   | [最大子序和](https://leetcode-cn.com/problems/maximum-subarray/) | [Python](./20190917/20190918/readme.md#Python)✅ [C++](./20190917/20190918/readme.md#C)✅ | ★    | 2019.09.18 | 分治法、动态规划         |
| 66   | [加一](https://leetcode-cn.com/problems/plus-one/)           | [Python](./20190917/20190918/readme.md#Python-1)✅ [C++](./20190917/20190918/readme.md#C-1)✅ | ★    | 2019.09.18 |                          |
| 88   | [合并两个有序数组](https://leetcode-cn.com/problems/merge-sorted-array/) | [Python](./20190917/20190919/readme.md#Python)✅ [C++](./20190917/20190919/readme.md#C)✅ | ★    | 2019.09.19 | 双指针                   |
| 118  | [杨辉三角](https://leetcode-cn.com/problems/pascals-triangle/) | [Python](./20190917/20190920/readme.md#Python)✅ [C++](./20190917/20190920/readme.md#C)✅ | ★    | 2019.09.20 | 动态规划，递归           |
| 119  | [杨辉三角 II](https://leetcode-cn.com/problems/pascals-triangle-ii/) | [Python](./20190917/20190920/readme.md#Python-1)✅ [C++](./20190917/20190920/readme.md#C-1)✅ | ★    | 2019.09.20 | 公式法                   |
| 121  | [买卖股票的最佳时机](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/) | [Python](./20190917/20190921/readme.md#Python)✅ [C++](./20190917/20190921/readme.md#C)✅ | ★    | 2019.09.21 | 动态规划                 |
| 122  | [买卖股票的最佳时机 II](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/) | [Python](./20190917/20190921/readme.md#Python-1)✅ [C++](./20190917/20190921/readme.md#C-1)✅ | ★    | 2019.09.21 |                          |
| 167  | [两数之和 II - 输入有序数组](https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/) | [Python](./20190917/20190921/readme.md#Python-2)✅ [C++](./20190917/20190921/readme.md#C-2)✅ | ★    | 2019.09.21 | 哈希表、双指针           |
| 169  | [求众数](https://leetcode-cn.com/problems/majority-element/) | [Python](./20190917/20190921/readme.md#Python-3)✅ [C++](./20190917/20190921/readme.md#C-3)✅ | ★    | 2019.09.21 | 哈希表、排序法、投票算法 |
| 189  | [旋转数组](https://leetcode-cn.com/problems/rotate-array/)   | [Python](./20190917/20190921/readme.md#Python-4)✅ [C++](./20190917/20190921/readme.md#C-4)✅ | ★    | 2019.09.21 |                          |
| 217  | [存在重复元素](https://leetcode-cn.com/problems/contains-duplicate/) | [Python](./20190917/20190921/readme.md#Python-5)✅ [C++](./20190917/20190921/readme.md#C-5)✅ | ★    | 2019.09.21 | 哈希表、排序法           |
| 219  | [存在重复元素 II](https://leetcode-cn.com/problems/contains-duplicate-ii/) | [Python](./20190917/20190921/readme.md#Python-6)✅ [C++](./20190917/20190921/readme.md#C-6)✅ | ★    | 2019.09.21 | 哈希表                   |
| 268  | [缺失数字](https://leetcode-cn.com/problems/missing-number/) | [Python](./20190917/20190922/readme.md#Python)✅ [C++](./20190917/20190922/readme.md#C)✅ | ★    | 2019.09.22 | 排序法、位运算           |
| 283  | [移动零](https://leetcode-cn.com/problems/move-zeroes/)      | [Python](./20190917/20190922/readme.md#Python-1)✅ [C++](./20190917/20190922/readme.md#C-1)✅ | ★    | 2019.09.22 | 双指针                   |
| 414  | [第三大的数](https://leetcode-cn.com/problems/third-maximum-number/) | [Python](./20190917/20190922/readme.md#Python-2)✅ [C++](./20190917/20190922/readme.md#C-2)✅ | ★    | 2019.09.22 |                          |
| 448  | [找到所有数组中消失的数字](https://leetcode-cn.com/problems/find-all-numbers-disappeared-in-an-array/) | [Python](./20190917/20190922/readme.md#Python-3)✅ [C++](./20190917/20190922/readme.md#C-3)✅ | ★    | 2019.09.22 | 标记法                   |
| 485  | [最大连续1的个数](https://leetcode-cn.com/problems/max-consecutive-ones/) | [Python](./20190917/20190922/readme.md#Python-4)✅ [C++](./20190917/20190922/readme.md#C-4)✅ | ★    | 2019.09.22 |                          |
| 509  | [斐波那契数](https://leetcode-cn.com/problems/fibonacci-number) | [Python](./20190917/20190923/readme.md#Python)✅ [C++](./20190917/20190923/readme.md#C)✅ | ★    | 2019.09.23 | 动态规划                 |
| 532  | [数组中的K-diff数对](https://leetcode-cn.com/problems/k-diff-pairs-in-an-array) | [Python](./20190917/20190923/readme.md#Python-1)✅ [C++](./20190917/20190923/readme.md#C-1)✅ | ★    | 2019.09.23 | 哈希表                   |
| 561  | [数组拆分 I](https://leetcode-cn.com/problems/array-partition-i) | [Python](./20190917/20190923/readme.md#Python-2)✅ [C++](./20190917/20190923/readme.md#C-2)✅ | ★    | 2019.09.23 | 排序法                   |
| 566  | [重塑矩阵](https://leetcode-cn.com/problems/reshape-the-matrix) | [Python](./20190917/20190923/readme.md#Python-3)✅ [C++](./20190917/20190923/readme.md#C-3)✅ | ★    | 2019.09.23 |                          |
| 581  | [最短无序连续子数组](https://leetcode-cn.com/problems/shortest-unsorted-continuous-subarray) | [Python](./20190917/20190923/readme.md#Python-4)✅ [C++](./20190917/20190923/readme.md#C-4)✅ | ★    | 2019.09.23 |                          |
| 605  | [种花问题](https://leetcode-cn.com/problems/can-place-flowers) | [Python](./20190917/20190923/readme.md#Python-5)✅ [C++](./20190917/20190923/readme.md#C-5)✅ | ★    | 2019.09.23 |                          |
| 628  | [三个数的最大乘积](https://leetcode-cn.com/problems/maximum-product-of-three-numbers) | [Python](./20190917/20190923/readme.md#Python-6)✅ [C++](./20190917/20190923/readme.md#C-6)✅ | ★    | 2019.09.23 |                          |
| 643  | [子数组最大平均数 I](https://leetcode-cn.com/problems/maximum-average-subarray-i) | [Python](./20190917/20190923/readme.md#Python-7)✅ [C++](./20190917/20190923/readme.md#C-7)✅ | ★    | 2019.09.23 | 动态规划                 |
| 661  | [图片平滑器](https://leetcode-cn.com/problems/image-smoother) | [Python](./20190917/20190923/readme.md#Python-8)✅ [C++](./20190917/20190923/readme.md#C-8)✅ | ★    | 2019.09.23 | 偏移标识                 |
| 665  | [非递减数列](https://leetcode-cn.com/problems/non-decreasing-array/) | [Python](./20190917/20190923/readme.md#Python-9)⁉️ [C++](./20190917/20190923/readme.md#C-9)⁉️ | ★    | 2019.09.23 |                          |
| 674  | [最长连续递增序列](https://leetcode-cn.com/problems/longest-continuous-increasing-subsequence/) | [Python](./20190917/20190924/readme.md#Python)✅ [C++](./20190917/20190924/readme.md#C)✅ | ★    | 2019.09.24 |                          |
| 697  | [数组的度](https://leetcode-cn.com/problems/degree-of-an-array/) | [Python](./20190917/20190924/readme.md#Python-1)✅ [C++](./20190917/20190924/readme.md#C-1)✅ | ★    | 2019.09.24 |                          |
| 717  | [1比特与2比特字符](https://leetcode-cn.com/problems/1-bit-and-2-bit-characters) | [Python](./20190917/20190924/readme.md#Python-2)✅ [C++](./20190917/20190924/readme.md#C-2)✅ | ★    | 2019.09.24 |                          |
| 724  | [寻找数组的中心索引](https://leetcode-cn.com/problems/find-pivot-index) | [Python](./20190917/20190924/readme.md#Python-3)✅ [C++](./20190917/20190924/readme.md#C-3)✅ | ★    | 2019.09.24 |                          |
| 746  | [使用最小花费爬楼梯](https://leetcode-cn.com/problems/min-cost-climbing-stairs) | [Python](./20190917/20190924/readme.md#Python-4)✅ [C++](./20190917/20190924/readme.md#C-4)✅ | ★    | 2019.09.24 | 动态规划                 |
| 747  | [至少是其他数字两倍的最大数](https://leetcode-cn.com/problems/largest-number-at-least-twice-of-others/) | [Python](./20190917/20190925/readme.md#Python)✅ [C++](./20190917/20190925/readme.md#C)✅ | ★    | 2019.09.25 |                          |
| 766  | [托普利茨矩阵](https://leetcode-cn.com/problems/toeplitz-matrix/) | [Python](./20190917/20190925/readme.md#Python-1)✅ [C++](./20190917/20190925/readme.md#C-1)✅ | ★    | 2019.09.25 |                          |
| 830  | [较大分组的位置](https://leetcode-cn.com/problems/positions-of-large-groups/) | [Python](./20190917/20190925/readme.md#Python-2)✅ [C++](./20190917/20190925/readme.md#C-2)✅ | ★    | 2019.09.25 |                          |
| 832  | [翻转图像](https://leetcode-cn.com/problems/flipping-an-image/) | [Python](./20190917/20190925/readme.md#Python-3)✅ [C++](./20190917/20190925/readme.md#C-3)✅ | ★    | 2019.09.25 |                          |
| 840  | [矩阵中的幻方](https://leetcode-cn.com/problems/magic-squares-in-grid/) |                                                              | ★    | 2019.09.25 | 暴力法 无意义            |
| 849  | [到最近的人的最大距离](https://leetcode-cn.com/problems/maximize-distance-to-closest-person/) | [Python](./20190917/20190926/readme.md#Python)✅ [C++](./20190917/20190926/readme.md#C)✅ | ★    | 2019.09.26 |                          |
| 867  | [转置矩阵](https://leetcode-cn.com/problems/transpose-matrix/) | [Python](./20190917/20190926/readme.md#Python-1)✅ [C++](./20190917/20190926/readme.md#C-1)✅ | ★    | 2019.09.26 |                          |
| 888  | [公平的糖果交换](https://leetcode-cn.com/problems/fair-candy-swap/) | [Python](./20190917/20190926/readme.md#Python-2)✅ [C++](./20190917/20190926/readme.md#C-2)✅ | ★    | 2019.09.26 |                          |
| 896  | [单调数列](https://leetcode-cn.com/problems/monotonic-array/) | [Python](./20190917/20190926/readme.md#Python-3)✅ [C++](./20190917/20190926/readme.md#C-3)✅ | ★    | 2019.09.26 |                          |
| 905  | [按奇偶排序数组](https://leetcode-cn.com/problems/sort-array-by-parity/) | [Python](./20190917/20190926/readme.md#Python-4)✅ [C++](./20190917/20190926/readme.md#C-4)✅ | ★    | 2019.09.26 | 双指针                   |
| 914  | [卡牌分组](https://leetcode-cn.com/problems/x-of-a-kind-in-a-deck-of-cards/) | [Python](./20190917/20190927/readme.md#Python)✅ [C++](./20190917/20190927/readme.md#C)✅ | ★    | 2019.09.27 |                          |
| 922  | [按奇偶排序数组 II](https://leetcode-cn.com/problems/sort-array-by-parity-ii/) | [Python](./20190917/20190927/readme.md#Python-1)✅ [C++](./20190917/20190927/readme.md#C-1)✅ | ★    | 2019.09.27 |                          |
| 941  | [有效的山脉数组](https://leetcode-cn.com/problems/valid-mountain-array/) | [Python](./20190917/20190928/readme.md#Python)✅ [C++](./20190917/20190928/readme.md#C)✅ | ★    | 2019.09.28 |                          |
| 977  | [有序数组的平方](https://leetcode-cn.com/problems/squares-of-a-sorted-array/) | [Python](./20190917/20190928/readme.md#Python-1)✅ [C++](./20190917/20190928/readme.md#C-1)✅ | ★    | 2019.09.28 |                          |
|      |                                                              |                                                              |      |            |                          |



## 2019.09

### 题目列表

|   #   | 题目                                                                                            | 题解                                            | 难度 | 时间       |
| :---: | ----------------------------------------------------------------------------------------------- | :---------------------------------------------- | ---- | ---------- |
|  15   | [三数之和](https://leetcode-cn.com/problems/3sum/)                                              | [Python](./201909/20190901/readme.md#Python)❎   | ★★   | 2019.09.01 |
|  16   | [最接近的三数之和](https://leetcode-cn.com/problems/3sum-closest/)                              | [Python](./201909/20190902/readme.md#Python)✅   | ★★   | 2019.09.02 |
|  17   | [电话号码的字母组合](https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/)   | [Python](./201909/20190903/readme.md#Python)✅   | ★★   | 2019.09.03 |
|  18   | [四数之和](https://leetcode-cn.com/problems/4sum/)                                              | [Python](./201909/20190904/readme.md#Python)✅   | ★★   | 2019.09.04 |
|  19   | [删除链表的倒数第N个节点](https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/)   | [Python](./201909/20190906/readme.md#Python)✅   | ★★   | 2019.09.06 |
|  20   | [有效的括号](https://leetcode-cn.com/problems/valid-parentheses/)                               | [Python](./201909/20190907/readme.md#Python)✅   | ★    | 2019.09.07 |
|  21   | [合并两个有序链表](https://leetcode-cn.com/problems/merge-two-sorted-lists/)                    | [Python](./201909/20190907/readme.md#Python-1)✅ | ★    | 2019.09.07 |
|  22   | [括号生成](https://leetcode-cn.com/problems/generate-parentheses/)                              | [Python](./201909/20190908/readme.md#Python)✅   | ★★   | 2019.09.08 |
|  23   | [合并K个排序列表](https://leetcode-cn.com/problems/merge-k-sorted-lists/)                       | [Python](./201909/20190909/readme.md#Python)✅   | ★★★  | 2019.09.09 |
|  24   | [两两交换链表中的节点](https://leetcode-cn.com/problems/swap-nodes-in-pairs/)                   | [Python](./201909/20190912/readme.md#Python)✅   | ★★   | 2019.09.12 |
|  25   | [K 个一组翻转链表](https://leetcode-cn.com/problems/reverse-nodes-in-k-group/)                  | [Python](./201909/20190914/readme.md#Python)⁉️  | ★★★  | 2019.09.14 |
|  26   | [删除排序数组中的重复项](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/) | [Python](./201909/20190916/readme.md#Python)✅   | ★    | 2019.09.16 |

### 总结

- (25.)  K 个一组翻转链表

  >  不完全理解

  

### 忘记的原因

1. 2019.09.05
   - 偷懒的一天
2. 2019.09.10
   - 聚餐休息一天
3. 2019.09.11
   - 忘记练习的一天
4. 2019.09.13
   - 中秋放假
5. 2019.09.15
   - 捣鼓电脑，然后一堆杂事给搞漏了



## 2019.08

### 题目列表

|   #   | 题目                                                                                                     | 题解                                             | 难度 | 时间       |
| :---: | -------------------------------------------------------------------------------------------------------- | :----------------------------------------------- | ---- | ---------- |
|   1   | [两数之和](https://leetcode-cn.com/problems/two-sum/)                                                    | [Python](./201908/20190825/readme.md#Python)✅    | ★    | 2019.08.25 |
|   2   | [两数相加](https://leetcode-cn.com/problems/add-two-numbers/)                                            | [Python](./201908/20190825/readme.md#Python-1)✅  | ★★   | 2019.08.25 |
|   3   | [无重复字符的最长子串](https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/) | [Python](./201908/20190825/readme.md#Python-2)✅  | ★★   | 2019.08.25 |
|   4   | [寻找两个有序数组的中位数](https://leetcode-cn.com/problems/median-of-two-sorted-arrays/)                | [Python](./201908/20190826/readme.md#Python)❎    | ★★★  | 2019.08.26 |
|   5   | [最长回文子串](https://leetcode-cn.com/problems/longest-palindromic-substring/)                          | [Python](./201908/20190826/readme.md#Python-1)⁉️ | ★★   | 2019.08.26 |
|   6   | [Z 字形转换](https://leetcode-cn.com/problems/zigzag-conversion/)                                        | [Python](./201908/20190826/readme.md#Python-2)✅  | ★★   | 2019.08.26 |
|   7   | [整数反转](https://leetcode-cn.com/problems/reverse-integer/)                                            | [Python](./201908/20190827/readme.md#Python)✅    | ★    | 2019.08.27 |
|   8   | [字符串转换整数(atoi)](https://leetcode-cn.com/problems/string-to-integer-atoi/)                         | [Python](./201908/20190827/readme.md#Python-1)✅  | ★★   | 2019.08.27 |
|   9   | [回文数](https://leetcode-cn.com/problems/palindrome-number/)                                            | [Python](./201908/20190828/readme.md#Python)✅    | ★    | 2019.08.28 |
|  10   | [正则表达式匹配](https://leetcode-cn.com/problems/regular-expression-matching/)                          | [Python](./201908/20190828/readme.md#Python-1)⁉️ | ★★★  | 2019.08.28 |
|  11   | [盛最多水的容器](https://leetcode-cn.com/problems/container-with-most-water/)                            | [Python](./201908/20190829/readme.md#Python)✅    | ★★   | 2019.08.29 |
|  12   | [整数转罗马数字](https://leetcode-cn.com/problems/integer-to-roman/)                                     | [Python](./201908/20190830/readme.md#Python)✅    | ★★   | 2019.08.30 |
|  13   | [罗马数字转整数](https://leetcode-cn.com/problems/roman-to-integer/)                                     | [Python](./201908/20190831/readme.md#Python)✅    | ★    | 2019.08.31 |
|  14   | [最长公共前缀](https://leetcode-cn.com/problems/longest-common-prefix/)                                  | [Python](./201908/20190831/readme.md#Python-1)✅  | ★    | 2019.08.31 |



### 总结

1. 动态规划问题，还需要理解
2. 时间复杂度的计算和空间复杂度的计算整理