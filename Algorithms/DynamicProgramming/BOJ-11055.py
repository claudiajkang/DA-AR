from sys import stdin
read = lambda: stdin.readline().rstrip()

N = int(read())
A = list(map(int, read().split()))
DP = [0] * N

for i in range(N):
    for j in range(0, i):
        if A[j] < A[i]:
            DP[i] = max(DP[j], DP[i])

    DP[i] += A[i]

print(max(DP))
