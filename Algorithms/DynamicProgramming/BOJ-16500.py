from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)
read = lambda: stdin.readline().rstrip()

S = read()
N = int(read())
A = []
dp = [0] * 101

for i in range(N):
    A.append(read())

dp[len(S)] = 1

for pos in range(len(S) - 1, -1, -1):
    for j in range(0, N):
        if (S.find(A[j], pos)) == pos and dp[pos + len(A[j])] == 1:
            dp[pos] = 1
            break

        else:
            dp[pos] = 0

print(dp[0])