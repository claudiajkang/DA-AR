from sys import stdin
read = lambda: stdin.readline().rstrip()

n = int(input())
h = [0] * 1001

for _ in range(n):
    x, y = map(int, read().split())
    h[x] = y

highest_index = h.index(max(h))
now_max = 0
c = 0
s = 0
for i in range(0, highest_index):
    if now_max < h[i]:
        now_max = h[i]
    s += now_max

now_max = 0
for i in range(1000, highest_index, -1):
    if now_max < h[i]:
        now_max = h[i]
    s += now_max

print(s+max(h))