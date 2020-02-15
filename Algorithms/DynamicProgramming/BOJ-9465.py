from sys import stdin
  
T = int(stdin.readline())

for i in range(T):
    n = int(stdin.readline())
    a = [[],[]]
    a[0] = list(map(int, stdin.readline().strip().split()))
    a[1] = list(map(int, stdin.readline().strip().split()))

    dp = [[0 for l in range(n)] for j in range(2)]

    dp[0][0], dp[1][0] = a[0][0], a[1][0]
    dp[0][1] = dp[1][0] + a[0][1]
    dp[1][1] = dp[0][0] + a[1][1]

    for k in range(2, n):
        dp[0][k] = max(dp[1][k-1], dp[1][k-2]) + a[0][k]
        dp[1][k] = max(dp[0][k-1], dp[0][k-2]) + a[1][k]

    print(max(dp[0][n-1], dp[1][n-1]))
