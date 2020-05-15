from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)


def Comb(n, k):
    global C, N, MOD

    if C[n][k]:
        return C[n][k]
    if k == 0 or k == n:
        C[n][k] = 1
        return C[n][k]
    C[n][k] = (Comb(n - 1, k - 1) + Comb(n - 1, k)) % MOD
    return C[n][k]


N, K = map(int, stdin.readline().rstrip().split())
MOD = 10007
C = [[0] * 1001 for i in range(1001)]

print(Comb(N, K))
