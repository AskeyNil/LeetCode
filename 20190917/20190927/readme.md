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


