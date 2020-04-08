from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)

read = lambda: stdin.readline().rstrip()


def dfs(nnum):
    global island

    sum = 0

    for i in range(len(island[nnum].connect)):
        sum += dfs(island[nnum].connect[i])

    if island[nnum].type == 'S':
        return island[nnum].data + sum

    else:
        return (sum - island[nnum].data) if (sum - island[nnum].data) >= 0 else 0


class Node:
    def __init__(self):
        self.data = 0
        self.type = 'S'
        self.connect = []


n = int(read())
island = [Node() for i in range(n + 1)]

for i in range(2, n + 1):
    t, a, p = read().split()
    island[i].type = t
    island[i].data = int(a)
    island[int(p)].connect.append(i)

print(dfs(1))
