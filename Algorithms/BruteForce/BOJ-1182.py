from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)
read = lambda: stdin.readline().rstrip()


def dfs(cur):
    global N, cnt, curSum, val, S
    if cur == N: return

    if curSum + val[cur] == S:
        cnt += 1

    dfs(cur + 1)
    curSum += val[cur]

    dfs(cur + 1)

    curSum -= val[cur]


N, S = map(int, read().split())
val = list(map(int, read().split()))

cnt = 0
curSum = 0
dfs(0)
print(cnt)
