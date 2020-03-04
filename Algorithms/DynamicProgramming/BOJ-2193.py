from sys import stdin

N = int(stdin.readline())
DP = [0, 1, 1, 2] + [0 for _ in range(4, 91)]

if N > 90 or N < 1:
    print(0)

else:
    if N > 3:
        for i in range(4, N+1):
            DP[i] = DP[i-1] + DP[i-2]

    print(DP[N])
