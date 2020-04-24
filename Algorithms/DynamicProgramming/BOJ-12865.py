from sys import stdin

read = lambda: stdin.readline().rstrip()

N, K = map(int, read().split())
W = [0] * (N + 1)
V = [0] * (N + 1)
dp = [[0] * (K + 1) for i in range(N + 1)]

for i in range(1, N + 1):
    W[i], V[i] = map(int, read().split())

for i in range(1, N + 1):
    for j in range(1, K + 1):

        if j < W[i]:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(V[i] + dp[i - 1][j - W[i]], dp[i - 1][j])

print(dp[N][K])
