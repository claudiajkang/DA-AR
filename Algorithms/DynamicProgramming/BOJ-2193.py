from sys import stdin

N = int(stdin.readline())
DP = [0, 1, 1, 2] + [0 for _ in range(4, 91)]

if 3 < N <= 90:
    for i in range(4, N+1):
        DP[i] = DP[i-2] + DP[i-1]

print(DP[N])
