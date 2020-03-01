import sys
sys.setrecursionlimit(10**6)


V = int(sys.stdin.readline().rstrip())
g = [[]for _ in range(V + 1)]
visited = [False for _ in range(V + 1)]

# 입력 처리
for i in range(1, V + 1):
    e = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in range(1, len(e)-1, 2):
        g[e[0]].append((e[j], e[j + 1]))


def dfs(v, dist):
    ret = (v, dist)
    visited[v] = True

    for v_d in g[v]:
        if visited[v_d[0]]:
            continue

        next_search = dfs(v_d[0], dist + v_d[1])

        if ret[1] < next_search[1]:
            ret = next_search

    return ret


first_dfs = dfs(1, 0)
far_v = first_dfs[0]

visited = [False for _ in range(V + 1)]

second_dfs = dfs(far_v, 0)
far_v = second_dfs[1]
print(far_v)
