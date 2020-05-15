from sys import stdin
read = lambda: stdin.readline()

n = int(read())
pos = [[] for i in range(n)]

for i in range(n):
    pos[i] = list(map(int, read().split()))

pos.sort(key=lambda x: x[1])
pos.sort(key=lambda x: x[0])

for i, j in pos:
    print(f"{i} {j}")
