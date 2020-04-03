from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)

read = lambda: stdin.readline().rstrip()

n = int(read())
arr = [[] for i in range(n + 1)]
parent = [0] * (n + 1)

for i in range(n - 1):
    a, b = map(int, read().split())
    arr[a].append(b)
    arr[b].append(a)


def set_parent(node):
    for i in arr[node]:
        if parent[i] == 0:
            parent[i] = node
            set_parent(i)


set_parent(1)

for i in parent[2:]:
    print(i)
