import sys
  
n = int(sys.stdin.readline())

dp = [0 for i in range(n+1)]

for i in range(1, n+1):
    if 1 <= i <= 4:
        dp[i] = [1,3,5,11][i-1]
    else:
        dp[i] = 2*dp[i-2] + dp[i-1]

print(dp[n]%10007)

