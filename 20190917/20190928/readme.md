# 941. 有效的山脉数组

## [题目](https://leetcode-cn.com/problems/valid-mountain-array/)

<p>给定一个整数数组&nbsp;<code>A</code>，如果它是有效的山脉数组就返回&nbsp;<code>true</code>，否则返回 <code>false</code>。</p>
<p>让我们回顾一下，如果 A 满足下述条件，那么它是一个山脉数组：</p>
<ul>
	<li><code>A.length &gt;= 3</code></li>
	<li>在&nbsp;<code>0 &lt; i&nbsp;&lt; A.length - 1</code>&nbsp;条件下，存在&nbsp;<code>i</code>&nbsp;使得：
	<ul>
		<li><code>A[0] &lt; A[1] &lt; ... A[i-1] &lt; A[i] </code></li>
		<li><code>A[i] &gt; A[i+1] &gt; ... &gt; A[A.length - 1]</code></li>
	</ul>
	</li>
</ul>

<p>&nbsp;</p>
<p><strong>示例 1：</strong></p>
<pre><strong>输入：</strong>[2,1]
<strong>输出：</strong>false
</pre>

<p><strong>示例 2：</strong></p>
<pre><strong>输入：</strong>[3,5,5]
<strong>输出：</strong>false
</pre>

<p><strong>示例 3：</strong></p>
<pre><strong>输入：</strong>[0,3,2,1]
<strong>输出：</strong>true</pre>

<p>&nbsp;</p>
<p><strong>提示：</strong></p>
<ol>
	<li><code>0 &lt;= A.length &lt;= 10000</code></li>
	<li><code>0 &lt;= A[i] &lt;= 10000&nbsp;</code></li>
</ol>

<p>&nbsp;</p>
<p>&nbsp;</p>
## [Python](./941.%20有效的山脉数组.py)

``` python
class Solution:
    def validMountainArray(self, A: [int]) -> bool:
        is_down = False
        left = None
        length = len(A)
        for index, num in enumerate(A):
            if left is None:
                left = num
            else:
                if is_down:
                    if left < num:
                        return False
                else:
                    if left > num:
                        if index < 2:
                            return False
                        is_down = True
                    if index == length - 1:
                        return False
        return True
```


## [C++](./941.%20有效的山脉数组.cc)

``` c++
class Solution {
  public:
    bool validMountainArray(vector<int> &A) {
        if (A.size() < 3)
            return false;
        bool is_down = false;
        int left = A[0];
        for (int i = 1; i < A.size(); i++) {
            if (is_down) {
                if (left <= A[i]) {
                    return false;
                }
            } else {
                if (left > A[i]) {
                    if (i < 2) {
                        return false;
                    }
                    is_down = true;
                } else if (left == A[i]) {
                    return false;
                } else {
                    if (i == A.size() - 1) {
                        return false;
                    }
                }
            }
            left = A[i];
        }
        return true;
    }
};
```



# 977. 有序数组的平方

## [题目](https://leetcode-cn.com/problems/squares-of-a-sorted-array/)

<p>给定一个按非递减顺序排序的整数数组 <code>A</code>，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。</p>
<p>&nbsp;</p>
<p><strong>示例 1：</strong></p>
<pre><strong>输入：</strong>[-4,-1,0,3,10]
<strong>输出：</strong>[0,1,9,16,100]
</pre>

<p><strong>示例 2：</strong></p>
<pre><strong>输入：</strong>[-7,-3,2,3,11]
<strong>输出：</strong>[4,9,9,49,121]
</pre>

<p>&nbsp;</p>
<p><strong>提示：</strong></p>
<ol>
	<li><code>1 &lt;= A.length &lt;= 10000</code></li>
	<li><code>-10000 &lt;= A[i] &lt;= 10000</code></li>
	<li><code>A</code>&nbsp;已按非递减顺序排序。</li>
</ol>

## [Python](./977.%20有序数组的平方.py)

### 正常思路

``` python
class Solution:
    def sortedSquares(self, A: [int]) -> [int]:
        for index, num in enumerate(A):
            A[index] = num * num
        A.sort()
        return A
```

### Python特有一行法


``` python
class Solution:
    def sortedSquares(self, A: [int]) -> [int]:
        return sorted([num * num for num in A])
```

### 双指针法


``` python
class Solution:
    def sortedSquares(self, A: [int]) -> [int]:
        left = 0, A[0] ** 2
        right = len(A) - 1, A[len(A) - 1] ** 2
        B = [0 for _ in range(len(A))]
        index = right[0]
        while index >= 0:
            if left[1] < right[1]:
                B[index] = right[1]
                if right[0] != 0:
                    right = right[0] - 1, A[right[0] - 1] ** 2
            else:
                B[index] = left[1]
                if left[0] + 1 != len(A):
                    left = left[0] + 1, A[left[0] + 1] ** 2
            index -= 1
        return B

```

## [C++](./977.%20有序数组的平方.cc)

### 双指针法

``` c++
class Solution {
  public:
    vector<int> sortedSquares(vector<int> &A) {
        int left = 0, right = A.size() - 1;
        vector<int> B(A.size());
        for (int i = A.size() - 1; i >= 0; i--) {
            int leftValue = pow(A[left], 2), rightValue = pow(A[right], 2);
            if (leftValue < rightValue) {
                B[i] = rightValue;
                if (right != 0)
                    right -= 1;
            } else {
                B[i] = leftValue;
                if (left + 1 != A.size())
                    left += 1;
            }
        }
        return B;
    }
};
```


# 985. 查询后的偶数和

## [题目](https://leetcode-cn.com/problems/sum-of-even-numbers-after-queries/)

<p>给出一个整数数组&nbsp;<code>A</code>&nbsp;和一个查询数组&nbsp;<code>queries</code>。</p>

<p>对于第&nbsp;<code>i</code>&nbsp;次查询，有&nbsp;<code>val =&nbsp;queries[i][0], index&nbsp;= queries[i][1]</code>，我们会把&nbsp;<code>val</code>&nbsp;加到&nbsp;<code>A[index]</code>&nbsp;上。然后，第&nbsp;<code>i</code>&nbsp;次查询的答案是 <code>A</code> 中偶数值的和。</p>

<p><em>（此处给定的&nbsp;<code>index = queries[i][1]</code>&nbsp;是从 0 开始的索引，每次查询都会永久修改数组&nbsp;<code>A</code>。）</em></p>

<p>返回所有查询的答案。你的答案应当以数组&nbsp;<code>answer</code>&nbsp;给出，<code>answer[i]</code>&nbsp;为第&nbsp;<code>i</code>&nbsp;次查询的答案。</p>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre><strong>输入：</strong>A = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]]
<strong>输出：</strong>[8,6,2,4]
<strong>解释：</strong>
开始时，数组为 [1,2,3,4]。
将 1 加到 A[0] 上之后，数组为 [2,2,3,4]，偶数值之和为 2 + 2 + 4 = 8。
将 -3 加到 A[1] 上之后，数组为 [2,-1,3,4]，偶数值之和为 2 + 4 = 6。
将 -4 加到 A[0] 上之后，数组为 [-2,-1,3,4]，偶数值之和为 -2 + 4 = 2。
将 2 加到 A[3] 上之后，数组为 [-2,-1,3,6]，偶数值之和为 -2 + 6 = 4。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= A.length &lt;= 10000</code></li>
	<li><code>-10000 &lt;= A[i] &lt;= 10000</code></li>
	<li><code>1 &lt;= queries.length &lt;= 10000</code></li>
	<li><code>-10000 &lt;= queries[i][0] &lt;= 10000</code></li>
	<li><code>0 &lt;= queries[i][1] &lt; A.length</code></li>
</ol>


## [Python](./985.%20查询后的偶数和.py)

``` python

class Solution:
    def sumEvenAfterQueries(self, A: [int], queries: [[int]]) -> [int]:
        sum_start = 0
        for num in A:
            if num % 2 == 0:
                sum_start += num
        result = []
        for val, index in queries:
            if A[index] % 2 == 0:
                sum_start -= A[index]
            A[index] += val
            if A[index] % 2 == 0:
                sum_start += A[index]
            result.append(sum_start)
        return result

```


## [C++](./985.%20查询后的偶数和.cc)

``` c++

class Solution {
  public:
    vector<int> sumEvenAfterQueries(vector<int> &A,
                                    vector<vector<int>> &queries) {
        int sum = 0;
        for (auto num : A) {
            if (num % 2 == 0)
                sum += num;
        }
        vector<int> v;
        for (auto q : queries) {
            int val = q[0], index = q[1];
            if (A[index] % 2 == 0)
                sum -= A[index];
            A[index] += val;
            if (A[index] % 2 == 0)
                sum += A[index];
            v.push_back(sum);
        }
        return v;
    }
};
```


