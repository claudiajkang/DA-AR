from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)

read = lambda: stdin.readline().rstrip()


def dfs(idx):
    global arr, vt
    sum = 0
    for i in range(len(vt[idx])):
        sum += dfs(vt[idx][i])

    if arr[idx].type == 'S':
        return arr[idx].cnt + sum

    else:
        return (sum - arr[idx].cnt) if (sum - arr[idx].cnt) >= 0 else 0


class Node:
    def __init__(self, cnt, t):
        self.type = t
        self.cnt = cnt


n = int(read())
arr = []
vt = [[] for i in range(n + 1)]

for i in range(n+1):
    if i in [0, 1]:
        arr.append(Node(0, 'S'))
    else:
        t, a, p = read().split()
        arr.append(Node(int(a), t))
        p = int(p)
        vt[p].append(i)

print(dfs(1))