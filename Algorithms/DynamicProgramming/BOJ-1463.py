import sys
  
N = int(sys.stdin.readline())
m = 1000001
dp = [0 for i in range(m)]

for i in range(2, N+1):
    if i == 2 or i == 3:  
        dp[i] = 1
    else:
        d1 = dp[i-1] + 1
        d2 = [dp[int(i/2)]+1, m][i%2]
        d3 = [dp[int(i/3)]+1, m, m][i%3]
        dp[i] = min(d1,d2,d3)

print(dp[N])
