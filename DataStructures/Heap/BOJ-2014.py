import sys
import heapq
import copy
input = sys.stdin.readline

K, N = map(int, input().split())
A = sorted(list(map(int, input().split())))
B = copy.deepcopy(A)
count = 0

while count < N-1:
    cur = heapq.heappop(B)

    for i in A:
        temp = cur * i
        heapq.heappush(B, temp)

        if cur % i == 0:
            break

    count += 1

print(heapq.heappop(B))