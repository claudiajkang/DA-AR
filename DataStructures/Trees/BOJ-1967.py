from collections import deque
from sys import stdin

read = lambda: stdin.readline().rstrip()


def dfs(start):
    global tree
    visited = [False] * (len(tree) + 1)
    visited[start] = True

    q = deque()
    q.append([start, 0])
    max_val = 0
    mi = start

    while q:
        ci, cd = q.popleft()

        if len(tree[ci]) == 0:
            break

        for ti, td in tree[ci]:
            if not visited[ti]:
                visited[ti] = True
                q.append([ti, td + cd])
                if (td + cd) > max_val:
                    max_val = td + cd
                    mi = ti

    return mi, max_val


n = int(read())
tree = [[] for i in range(n + 1)]
for i in range(n - 1):
    d, lr, v = map(int, read().split())
    tree[d].append([lr, v])
    tree[lr].append([d, v])

first_max_idx, res1 = dfs(1)
second_max_idx, res2 = dfs(first_max_idx)

print(res2)
