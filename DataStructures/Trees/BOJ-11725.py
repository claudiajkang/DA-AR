from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)

read = lambda: stdin.readline()

n = int(read())
tree = [[] for i in range(n + 1)]
parent = [0, 1] + [0] * (n - 1)

for i in range(1, n):
    a, b = map(int, read().split())
    tree[a].append(b)
    tree[b].append(a)


def set_parent(node):
    for i in tree[node]:
        if parent[i] == 0:
            parent[i] = node
            set_parent(i)


set_parent(1)
print('\n'.join(map(str, parent[2:])))
