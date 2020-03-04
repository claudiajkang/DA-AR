from sys import stdin
read = lambda : int(stdin.readline())

N = read()
DP = [0, 1, 1] + [0 for _ in range(3, N+1)]

if 3 <= N <= 90:
    for i in range(3, N+1):
        DP[i] = DP[i-1] + DP[i-2]

print(DP[N])
