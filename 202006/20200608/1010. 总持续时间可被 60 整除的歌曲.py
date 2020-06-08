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
