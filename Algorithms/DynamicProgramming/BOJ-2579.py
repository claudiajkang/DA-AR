from sys import stdin
read = lambda : int(stdin.readline())

N = read()
step = [0 for _ in range(301)]
DP = [0 for _ in range(301)]

for i in range(1, N+1):
    step[i] = read()

DP[1] = step[1]
DP[2] = max(DP[1] + step[2], step[2])

if N >= 3:
    for i in range(3, N+1):
        V2 = step[i] + DP[i-2]
        V3 = step[i] + step[i-1] + DP[i-3]
        DP[i] = max(V2, V3)

print(DP[N])
