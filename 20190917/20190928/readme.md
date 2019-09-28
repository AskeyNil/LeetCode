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


