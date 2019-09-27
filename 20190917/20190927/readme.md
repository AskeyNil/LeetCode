# 914. 卡牌分组

## [题目](https://leetcode-cn.com/problems/x-of-a-kind-in-a-deck-of-cards/)

<p>给定一副牌，每张牌上都写着一个整数。</p>
<p>此时，你需要选定一个数字 <code>X</code>，使我们可以将整副牌按下述规则分成 1 组或更多组：</p>
<ul>
	<li>每组都有&nbsp;<code>X</code>&nbsp;张牌。</li>
	<li>组内所有的牌上都写着相同的整数。</li>
</ul>

<p>仅当你可选的 <code>X &gt;= 2</code> 时返回&nbsp;<code>true</code>。</p>
<p>&nbsp;</p>
<p><strong>示例 1：</strong></p>
<pre><strong>输入：</strong>[1,2,3,4,4,3,2,1]
<strong>输出：</strong>true
<strong>解释：</strong>可行的分组是 [1,1]，[2,2]，[3,3]，[4,4]
</pre>

<p><strong>示例 2：</strong></p>
<pre><strong>输入：</strong>[1,1,1,2,2,2,3,3]
<strong>输出：</strong>false
<strong>解释：</strong>没有满足要求的分组。
</pre>

<p><strong>示例 3：</strong></p>
<pre><strong>输入：</strong>[1]
<strong>输出：</strong>false
<strong>解释：</strong>没有满足要求的分组。
</pre>

<p><strong>示例 4：</strong></p>
<pre><strong>输入：</strong>[1,1]
<strong>输出：</strong>true
<strong>解释：</strong>可行的分组是 [1,1]
</pre>

<p><strong>示例 5：</strong></p>
<pre><strong>输入：</strong>[1,1,2,2,2,2]
<strong>输出：</strong>true
<strong>解释：</strong>可行的分组是 [1,1]，[2,2]，[2,2]
</pre>

<p><br>
<strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= deck.length &lt;= 10000</code></li>
	<li><code>0 &lt;= deck[i] &lt;&nbsp;10000</code></li>
</ol>

<p>&nbsp;</p>

## [Python](./914.%20卡牌分组.py)

``` python

class Solution:
    def hasGroupsSizeX(self, deck):
        dic = {}
        for num in deck:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
        g = -1
        # 获取出现次数
        for v in dic.values():
            if g == -1:
                g = v
            else:
                g = self.gcd(g, v)
        return g >= 2


```


## [C++](./914.%20卡牌分组.cc)

``` c++

class Solution {
  public:
    bool hasGroupsSizeX(vector<int> &deck) {
        map<int, int> dic;
        for (int num : deck) {
            dic[num] += 1;
        }
        int g = -1;
        for (auto v : dic) {
            if (g == -1) // g 给赋值第一个
                g = v.second;
            else
                g = gcd(g, v.second); // 一次判断最大公约数
        }
        return g >= 2; // 最大公约数只要大于 2 本题就是正确的
    }
    // 辗转相除法 获取最大公约数
    int gcd(int x, int y) { return x == 0 ? y : gcd(y % x, x); }
};

```


# 922. 按奇偶排序数组 II

## [题目](https://leetcode-cn.com/problems/sort-array-by-parity-ii/)

<p>给定一个非负整数数组&nbsp;<code>A</code>， A 中一半整数是奇数，一半整数是偶数。</p>
<p>对数组进行排序，以便当&nbsp;<code>A[i]</code> 为奇数时，<code>i</code>&nbsp;也是奇数；当&nbsp;<code>A[i]</code>&nbsp;为偶数时， <code>i</code> 也是偶数。</p>
<p>你可以返回任何满足上述条件的数组作为答案。</p>
<p>&nbsp;</p>
<p><strong>示例：</strong></p>
<pre><strong>输入：</strong>[4,2,5,7]
<strong>输出：</strong>[4,5,2,7]
<strong>解释：</strong>[4,7,2,5]，[2,5,4,7]，[2,7,4,5] 也会被接受。
</pre>

<p>&nbsp;</p>
<p><strong>提示：</strong></p>
<ol>
	<li><code>2 &lt;= A.length &lt;= 20000</code></li>
	<li><code>A.length % 2 == 0</code></li>
	<li><code>0 &lt;= A[i] &lt;= 1000</code></li>
</ol>

<p>&nbsp;</p>

## [Python](./922.%20按奇偶排序数组%20II.py)

### 借助数组求解

``` python
class Solution:
    def sortArrayByParityII(self, A: [int]) -> [int]:
        left = []
        for index, num in enumerate(A):
            if (num - index) % 2 != 0:
                if not left:
                    left.append(index)
                else:
                    if (num - A[left[-1]]) % 2 == 0:
                        left.append(index)
                    else:
                        A[index], A[left[-1]] = A[left[-1]], A[index]
                        left.pop()
        return A
```

### 双指针法


``` python
class Solution:
    def sortArrayByParityII(self, A: [int]) -> [int]:
        odd = 1
        even = 0
        length = len(A)
        while odd < length and even < length:
            print(odd, even)
            is_odd = (A[odd] - odd) % 2
            is_even = (A[even] - even) % 2
            if is_odd == 1 and is_even == 1:
                A[even], A[odd] = A[odd], A[even]
            if is_odd == is_even:
                odd += 2
                even += 2
            elif is_odd == 0:
                odd += 2
            elif is_even == 0:
                even += 2
        return A
```


## [C++](./922.%20按奇偶排序数组%20II.cc)

``` c++

class Solution {
  public:
    vector<int> sortArrayByParityII(vector<int> &A) {
        vector<int> v;
        for (int i = 0; i < A.size(); i++) {
            if ((A[i] - i) % 2 != 0) {
                if (v.size() == 0) {
                    v.push_back(i);
                } else {
                    if ((A[i] - A[v[0]]) % 2 == 0) {
                        v.push_back(i);
                    } else {
                        cout << A[i] << " " << A[v[0]] << endl;
                        A[i] = A[i] + A[v[0]];
                        A[v[0]] = A[i] - A[v[0]];
                        A[i] = A[i] - A[v[0]];
                        cout << A[i] << " " << A[v[0]] << endl;
                        cout << endl;
                        v.erase(v.begin());
                    }
                }
            }
        }
        return A;
    }
};

```


