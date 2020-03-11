import sys

sys.setrecursionlimit(10 ** 6)


def dp(i):
    global res, p, q
    if i in res.keys():
        return res[i]
    else:
        res[i] = dp(i // p) + dp(i // q)
        return res[i]


n, p, q = map(int, sys.stdin.readline().split())
res = {0: 1}

print(dp(n))
