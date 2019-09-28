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


# 989. 数组形式的整数加法

## [题目](https://leetcode-cn.com/problems/add-to-array-form-of-integer/)

<p>对于非负整数&nbsp;<code>X</code>&nbsp;而言，<em><code>X</code></em>&nbsp;的<em>数组形式</em>是每位数字按从左到右的顺序形成的数组。例如，如果&nbsp;<code>X = 1231</code>，那么其数组形式为&nbsp;<code>[1,2,3,1]</code>。</p>
<p>给定非负整数 <code>X</code> 的数组形式&nbsp;<code>A</code>，返回整数&nbsp;<code>X+K</code>&nbsp;的数组形式。</p>
<p>&nbsp;</p>
<ol>
</ol>

<p><strong>示例 1：</strong></p>
<pre><strong>输入：</strong>A = [1,2,0,0], K = 34
<strong>输出：</strong>[1,2,3,4]
<strong>解释：</strong>1200 + 34 = 1234
</pre>

<p><strong>解释 2：</strong></p>
<pre><strong>输入：</strong>A = [2,7,4], K = 181
<strong>输出：</strong>[4,5,5]
<strong>解释：</strong>274 + 181 = 455
</pre>

<p><strong>示例 3：</strong></p>
<pre><strong>输入：</strong>A = [2,1,5], K = 806
<strong>输出：</strong>[1,0,2,1]
<strong>解释：</strong>215 + 806 = 1021
</pre>

<p><strong>示例 4：</strong></p>
<pre><strong>输入：</strong>A = [9,9,9,9,9,9,9,9,9,9], K = 1
<strong>输出：</strong>[1,0,0,0,0,0,0,0,0,0,0]
<strong>解释：</strong>9999999999 + 1 = 10000000000
</pre>

<p>&nbsp;</p>
<p><strong>提示：</strong></p>
<ol>
	<li><code>1 &lt;= A.length &lt;= 10000</code></li>
	<li><code>0 &lt;= A[i] &lt;= 9</code></li>
	<li><code>0 &lt;= K &lt;= 10000</code></li>
	<li>如果&nbsp;<code>A.length &gt; 1</code>，那么&nbsp;<code>A[0] != 0</code></li>
</ol>


## [Python](./989.%20数组形式的整数加法.py)

``` python
class Solution:
    def addToArrayForm(self, A: [int], K: int) -> [int]:
        return list(str(int("".join([str(num) for num in A])) + K))
```


## [C++](./989.%20数组形式的整数加法.cc)

``` c++
class Solution {
  public:
    vector<int> addToArrayForm(vector<int> &A, int K) {
        int carry = 0;
        for (int i = A.size() - 1; i >= 0; i--) {
            A[i] += K % 10 + carry;
            carry = 0;
            if (A[i] >= 10) {
                A[i] %= 10;
                carry = 1;
            }
            K /= 10;
        }
        while (K > 0) {
            A.insert(A.begin(), K % 10 + carry);
            carry = 0;
            if (A[0] >= 10) {
                A[0] %= 10;
                carry = 1;
            }
            K /= 10;
        }
        if (carry == 1)
            A.insert(A.begin(), 1);
        return A;
    }
};
```
# 999. 车的可用捕获量

## [题目](https://leetcode-cn.com/problems/available-captures-for-rook/)

<p>在一个 8 x 8 的棋盘上，有一个白色车（rook）。也可能有空方块，白色的象（bishop）和黑色的卒（pawn）。它们分别以字符 &ldquo;R&rdquo;，&ldquo;.&rdquo;，&ldquo;B&rdquo; 和 &ldquo;p&rdquo; 给出。大写字符表示白棋，小写字符表示黑棋。</p>
<p>车按国际象棋中的规则移动：它选择四个基本方向中的一个（北，东，西和南），然后朝那个方向移动，直到它选择停止、到达棋盘的边缘或移动到同一方格来捕获该方格上颜色相反的卒。另外，车不能与其他友方（白色）象进入同一个方格。</p>
<p>返回车能够在一次移动中捕获到的卒的数量。<br>
&nbsp;</p>

<p><strong>示例 1：</strong></p>
<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/02/23/1253_example_1_improved.PNG" style="height: 305px; width: 300px;"></p>
<pre><strong>输入：</strong>[[&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;],[&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;p&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;],[&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;R&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;p&quot;],[&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;],[&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;],[&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;p&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;],[&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;],[&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;]]
<strong>输出：</strong>3
<strong>解释：
</strong>在本例中，车能够捕获所有的卒。
</pre>

<p><strong>示例 2：</strong></p>
<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/02/23/1253_example_2_improved.PNG" style="height: 306px; width: 300px;"></p>
<pre><strong>输入：</strong>[[&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;],[&quot;.&quot;,&quot;p&quot;,&quot;p&quot;,&quot;p&quot;,&quot;p&quot;,&quot;p&quot;,&quot;.&quot;,&quot;.&quot;],[&quot;.&quot;,&quot;p&quot;,&quot;p&quot;,&quot;B&quot;,&quot;p&quot;,&quot;p&quot;,&quot;.&quot;,&quot;.&quot;],[&quot;.&quot;,&quot;p&quot;,&quot;B&quot;,&quot;R&quot;,&quot;B&quot;,&quot;p&quot;,&quot;.&quot;,&quot;.&quot;],[&quot;.&quot;,&quot;p&quot;,&quot;p&quot;,&quot;B&quot;,&quot;p&quot;,&quot;p&quot;,&quot;.&quot;,&quot;.&quot;],[&quot;.&quot;,&quot;p&quot;,&quot;p&quot;,&quot;p&quot;,&quot;p&quot;,&quot;p&quot;,&quot;.&quot;,&quot;.&quot;],[&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;],[&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;]]
<strong>输出：</strong>0
<strong>解释：
</strong>象阻止了车捕获任何卒。
</pre>

<p><strong>示例 3：</strong></p>
<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/02/23/1253_example_3_improved.PNG" style="height: 305px; width: 300px;"></p>
<pre><strong>输入：</strong>[[&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;],[&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;p&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;],[&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;p&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;],[&quot;p&quot;,&quot;p&quot;,&quot;.&quot;,&quot;R&quot;,&quot;.&quot;,&quot;p&quot;,&quot;B&quot;,&quot;.&quot;],[&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;],[&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;B&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;],[&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;p&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;],[&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;]]
<strong>输出：</strong>3
<strong>解释： </strong>
车可以捕获位置 b5，d6 和 f5 的卒。
</pre>

<p>&nbsp;</p>
<p><strong>提示：</strong></p>
<ol>
	<li><code>board.length == board[i].length == 8</code></li>
	<li><code>board[i][j]</code> 可以是&nbsp;<code>&#39;R&#39;</code>，<code>&#39;.&#39;</code>，<code>&#39;B&#39;</code>&nbsp;或&nbsp;<code>&#39;p&#39;</code></li>
	<li>只有一个格子上存在&nbsp;<code>board[i][j] == &#39;R&#39;</code></li>
</ol>


## [Python](./999.%20车的可用捕获量.py)

``` python
class Solution:
    def numRookCaptures(self, board: [[str]]) -> int:
        # 首先找到 白色车的位置
        for i, line in enumerate(board):
            for j, item in enumerate(line):
                if item == "R":
                    R_index = (i, j)
        # 定义 4 个方向向量
        direction = ((1, 0), (-1, 0), (0, 1), (0, -1))
        count = 0
        for direc in direction:
            index = R_index
            while True:
                index = index[0] + direc[0], index[1] + direc[1]
                # 判断越界
                if index[0] < 0 or index[0] > 7 or index[1] < 0 or index[1] > 7:
                    break
                if board[index[0]][index[1]] == "B":
                    break
                if board[index[0]][index[1]] == "p":
                    count += 1
                    break
        return count

```


## [C++](./999.%20车的可用捕获量.cc)

``` c++
class Solution {
  public:
    int numRookCaptures(vector<vector<char>> &board) {
        int x, y, count = 0;
        for (int i = 0; i < 8; i++) {
            for (int j = 0; j < 8; j++) {
                if (board[i][j] == 'R')
                    x = i, y = j;
            }
        }
        vector<vector<int>> direction{{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        for (auto v : direction) {
            int x1 = x, y1 = y;
            while (true) {
                x1 += v[0], y1 += v[1];
                if (x1 < 0 || x1 > 7 || y1 < 0 || y1 > 7)
                    break;
                if (board[x1][y1] == 'B')
                    break;
                if (board[x1][y1] == 'p') {
                    count += 1;
                    break;
                }
            }
        }
        return count;
    }
};
```


# 1002. 查找常用字符

## [题目](https://leetcode-cn.com/problems/find-common-characters/)

<p>给定仅有小写字母组成的字符串数组 <code>A</code>，返回列表中的每个字符串中都显示的全部字符（<strong>包括重复字符</strong>）组成的列表。例如，如果一个字符在每个字符串中出现 3 次，但不是 4 次，则需要在最终答案中包含该字符 3 次。</p>
<p>你可以按任意顺序返回答案。</p>
<p>&nbsp;</p>
<p><strong>示例 1：</strong></p>
<pre><strong>输入：</strong>[&quot;bella&quot;,&quot;label&quot;,&quot;roller&quot;]
<strong>输出：</strong>[&quot;e&quot;,&quot;l&quot;,&quot;l&quot;]
</pre>

<p><strong>示例 2：</strong></p>
<pre><strong>输入：</strong>[&quot;cool&quot;,&quot;lock&quot;,&quot;cook&quot;]
<strong>输出：</strong>[&quot;c&quot;,&quot;o&quot;]
</pre>

<p>&nbsp;</p>
<p><strong>提示：</strong></p>
<ol>
	<li><code>1 &lt;= A.length &lt;= 100</code></li>
	<li><code>1 &lt;= A[i].length &lt;= 100</code></li>
	<li><code>A[i][j]</code> 是小写字母</li>
</ol>


## [Python](./1002.%20查找常用字符.py)

``` python
class Solution:
    def commonChars(self, A: [str]) -> [str]:
        # 统计法
        counts = []
        for string in A:
            counts.append({})
            for char in string:
                if char in counts[-1]:
                    counts[-1][char] += 1
                else:
                    counts[-1][char] = 1
        result = []
        # 统计完了 遍历第一个字典
        for key in counts[0]:
            number = counts[0][key]
            is_add = True
            for dic in counts[0:]:
                if key not in dic:
                    is_add = False
                    break
                else:
                    if dic[key] < number:
                        number = dic[key]
            if is_add:
                for _ in range(number):
                    result.append(key)
        return result
```


## [C++](./1002.%20查找常用字符.cc)

``` c++
class Solution {
  public:
    vector<string> commonChars(vector<string> &A) {
        vector<map<string, int>> counts;
        for (string &str : A) {
            map<string, int> m;
            for (char &c : str) {
                string s{c};
                m[s] += 1;
            }
            counts.push_back(m);
        }
        vector<string> result;
        // 遍历第一个字典
        for (auto &key : counts[0]) {
            int number = key.second;
            bool is_add = true;
            for (int i = 1; i < counts.size(); i++) {
                auto &value = counts[i];
                if (value.find(key.first) == value.end()) {
                    is_add = false;
                    break;
                } else {
                    if (value[key.first] < number) {
                        number = value[key.first];
                    }
                }
            }
            if (is_add) {
                for (int j = 0; j < number; j++) {
                    result.push_back(key.first);
                }
            }
        }
        return result;
    }
};
```

## 总结

C++ 超时，应该用空间换时间，map 的效率比较低。

用 vector 去存取所有的字母，然后遍历，效率比用 map 存取单个更高。