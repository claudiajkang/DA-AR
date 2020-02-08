import sys
  
X = int(sys.stdin.readline())
m = 1000001
dp = [0 for i in range(m)]

for i in range(1, X+1):
    if i == 1:
        dp[i] = 0
    eif i in [2, 3]:  
        dp[i] = 1
    else:
        d2, d3 = m, m
        d1 = dp[i-1] + 1
        if i % 2 == 0:
            d2 = dp[int(i/2)] + 1
        if i % 3 == 0:
            d3 = dp[int(i/3)] + 1
        dp[i] = min(d1,d2,d3)

print(dp[X])
