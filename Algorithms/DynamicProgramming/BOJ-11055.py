from sys import stdin
read = lambda: stdin.readline().rstrip()

N = int(read())
A = list(map(int, read().split()))
DP = [0] * N

for i in range(N):
    for j in range(i-1, -1, -1):
        if A[j] < A[i]:
            DP[i] = max(DP[i], DP[j])

    DP[i] += A[i]

print(max(DP))
