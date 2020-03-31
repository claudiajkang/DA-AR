from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)

read = lambda: stdin.readline().rstrip()

def set_par(n):
    global parent, tree

    for i in tree[n]:
        if parent[i] == 0:
            parent[i] = n
            set_par(i)


n = int(read())
tree = [[] for i in range(n+1)]
parent = [0 for i in range(n+1)]
parent[1] = 1

for i in range(n - 1):
    a, b = map(int, read().split())
    tree[a].append(b)
    tree[b].append(a)

set_par(1)

for i in range(2, n+1):
    print(parent[i])
