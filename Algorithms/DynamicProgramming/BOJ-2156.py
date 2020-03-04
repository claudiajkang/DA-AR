from sys import stdin
read = lambda : int(stdin.readline())

N = read()
DP = [0 for _ in range(10001)]
G = [0 for _ in range(10001)]

for i in range(1, N+1):
    G[i] = read()

if 1 <= N <= 10000:
    DP[1] = G[1]
    DP[2] = max(G[2], DP[1]+G[2])

    for i in range(3, N+1):
        V1 = DP[i-1]
        V2 = G[i] + DP[i-2]
        V3 = G[i] + G[i-1] + DP[i-3]

        DP[i] = max(V1, V2, V3)

    print(DP[N])

else:
    print(0)