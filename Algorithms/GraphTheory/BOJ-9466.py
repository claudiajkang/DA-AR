from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)
read = lambda: stdin.readline().rstrip()


def dfs(cur):
    global s, visited, finished, cnt

    visited[cur] = True
    nxt = s[cur]

    if visited[nxt]:
        if not finished[nxt]:
            temp = nxt
            while temp != cur:
                temp = s[temp]
                cnt += 1

            cnt += 1

    else:
        dfs(nxt)

    finished[cur] = True


t = int(read())

for tt in range(t):
    n = int(read())
    s = [0] + list(map(int, read().split()))

    visited = [False] * (n + 1)
    finished = [False] * (n + 1)

    cnt = 0

    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i)

    print(n - cnt)
