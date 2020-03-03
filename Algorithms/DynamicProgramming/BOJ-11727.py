from sys import stdin

N = int(stdin.readline())
DP = [0 for _ in range(N+1)]

for i in range(1, N+1):
    if 1 <= i <= 2:
        DP[i] = [1, 3][i-1]

    else:
        DP[i] = DP[i-1] + DP[i-2] * 2

print(DP[N] % 10007)
