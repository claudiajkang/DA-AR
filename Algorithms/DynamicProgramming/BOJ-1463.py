from sys import stdin

N = int(stdin.readline())
DP = [0 for _ in range(10 ** 6 + 1)]

DP[2] = 1
DP[3] = 1

for i in range(4, N + 1):
    F = [DP[i - 1] + 1, DP[i - 1] + 1, DP[i - 1] + 1]
    F[0] = F[0] + 1

    if i % 2 == 0:
        F[1] = DP[i // 2] + 1
    if i % 3 == 0:
        F[2] = DP[i // 3] + 1

    DP[i] = min(F)

print(DP[N])
