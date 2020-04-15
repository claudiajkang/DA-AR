from collections import deque
from sys import stdin

read = lambda: stdin.readline().rstrip()

n = int(read())
time = [[] for i in range(n)]

for i in range(n):
    time[i] = list(map(int, read().split()))

time.sort(key=lambda x: x[0])
time.sort(key=lambda x: x[1])

before = 0
q = deque()

for i in range(n):
    if time[i][0] >= before:
        before = time[i][1]
        q.append(time[i])

print(len(q))
