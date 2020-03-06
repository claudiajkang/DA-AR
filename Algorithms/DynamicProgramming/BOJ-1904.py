from sys import stdin

N = int(stdin.readline())
DP = [0] * (N+2)

for i in range(1, N+1):
    if 1 <= i <= 3:
        DP[i] = [1, 2, 3][i-1]
    else:
        DP[i] = (DP[i-1] + DP[i-2]) % 15746

print(DP[N])
