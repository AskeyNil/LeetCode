# 1010. 总持续时间可被 60 整除的歌曲

## [题目](https://leetcode-cn.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/)

<p>在歌曲列表中，第 <code>i</code> 首歌曲的持续时间为 <code>time[i]</code> 秒。</p>

<p>返回其总持续时间（以秒为单位）可被 <code>60</code> 整除的歌曲对的数量。形式上，我们希望索引的数字 <code>i</code> 和 <code>j</code> 满足&nbsp; <code>i &lt; j</code> 且有&nbsp;<code>(time[i] + time[j]) % 60 == 0</code>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>[30,20,150,100,40]
<strong>输出：</strong>3
<strong>解释：</strong>这三对的总持续时间可被 60 整数：
(time[0] = 30, time[2] = 150): 总持续时间 180
(time[1] = 20, time[3] = 100): 总持续时间 120
(time[1] = 20, time[4] = 40): 总持续时间 60
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>[60,60,60]
<strong>输出：</strong>3
<strong>解释：</strong>所有三对的总持续时间都是 120，可以被 60 整数。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= time.length &lt;= 60000</code></li>
	<li><code>1 &lt;= time[i] &lt;= 500</code></li>
</ol>


## [Python](./1010.%20总持续时间可被%2060%20整除的歌曲.py)

``` python

class Solution:
    def numPairsDivisibleBy60(self, time: [int]) -> int:
        d = [0 for i in range(60)]
        for t in time:
            d[t % 60] += 1
        sum = 0
        sums = 0
        for index, value in enumerate(d):
            sums += value
            if index > 30:
                break
            if index != 30 and index != 0:
                sum += value * d[60 - index]
            else:
                sum += int(value * (value - 1) / 2)
        return sum

```


## [C++](./1010.%20总持续时间可被%2060%20整除的歌曲.cc)

``` c++

class Solution {
public:
    int numPairsDivisibleBy60(const vector<int> &time) {
        vector<int> v(60, 0);
        for (int value : time)
            v[value % 60] += 1;
        int sum = 0;
        for (auto i = 1; i < 30; i++)
            sum += v[i] * v[60 - i];
        sum += v[0] * (v[0] - 1) / 2;
        sum += v[30] * (v[30] - 1) / 2;
        return sum;
    }
};

```


