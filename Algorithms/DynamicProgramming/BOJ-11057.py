from sys import stdin

N = int(stdin.readline())
DP = [[0] * 10 for _ in range(N+1)]
DP[1] = [1] * 10

if N > 1:
    for i in range(2, N+1):
        DP[i][0] = DP[i-1][0]

        for j in range(1, 10):
            DP[i][j] = DP[i-1][j] + DP[i][j-1]

print(sum(DP[N]) % 10007)
