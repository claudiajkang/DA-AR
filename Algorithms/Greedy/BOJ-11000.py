from heapq import heappush, heappop
from sys import stdin

read = lambda: stdin.readline().rstrip()

N = int(read())
LECTURE = [[] for i in range(N)]

for i in range(N):
    LECTURE[i] = list(map(int, read().split()))

LECTURE.sort(key=lambda x: x[1])
LECTURE.sort(key=lambda x: x[0])

CLASSES = []

for i in range(N):
    if CLASSES and LECTURE[i][0] >= CLASSES[0]:
        heappop(CLASSES)

    heappush(CLASSES, LECTURE[i][1])

print(len(CLASSES))
