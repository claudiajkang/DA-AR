from sys import stdin
read = lambda : stdin.readline().rstrip()

N = int(read())
A = list(map(int, read().split()))
DP = [0] * N

DP[0] = 1
for i in range(1, N):
    for j in range(i-1, -1, -1):
        if A[i] > A[j]:
            DP[i] = max(DP[i], DP[j])

    DP[i] += 1

print(max(DP))
