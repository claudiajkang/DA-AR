from sys import stdin
from collections import deque
read = lambda : stdin.readline()

N = int(read())
NETN = int(read())
COM = [[] for _ in range(N+1)]

for i in range(NETN):
    A, B = map(int, read().split())
    COM[A].append(B)
    COM[B].append(A)

q = deque()
q.append(1)
dfs = []
dfs.append(1)

while len(q):
    cur = q.pop()

    for i in COM[cur]:
        if i not in dfs:
            dfs.append(i)
            q.append(i)

print(len(dfs)-1)
