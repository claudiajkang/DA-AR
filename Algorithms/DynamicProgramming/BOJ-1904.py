from sys import stdin

N = int(stdin.readline())
DP = [0] * (N+1)

for i in range(1, N+1):
    if i in [1, 2]:
        DP[i] = i
    else:
        DP[i] = (DP[i-1] + DP[i-2]) % 15746

print(DP[N])
