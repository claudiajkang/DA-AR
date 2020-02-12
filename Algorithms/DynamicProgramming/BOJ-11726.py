import sys
  
n = int(sys.stdin.readline())
dp = [0 for i in range(n+1)]

for i in range(1,n+1):
    if 1 <= i <= 4:
        dp[i] = [1,2,3,5][i-1]
    else:
        dp[i] = dp[i-1] + dp[i-2]

print(dp[n]%10007)
