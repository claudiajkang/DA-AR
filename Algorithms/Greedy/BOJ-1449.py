from sys import stdin

read = lambda: stdin.readline().rstrip()

n, l = map(int, read().split())
h = list(map(int, read().split()))
h.sort()

i = 0
c = 1
s = h[0]

while i < n:
    if h[i] < (s + l):
        i += 1
    else:
        s = h[i]
        c += 1

print(c)
