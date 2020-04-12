from sys import stdin
read = lambda: stdin.readline().rstrip()

n = int(read())
a = list(map(int, read().split()))
b = list(map(int, read().split()))

s = 0
for i in range(n):
    amax = a.index(max(a))
    bmin = b.index(min(b))
    s += (a[amax] * b[bmin])
    a.pop(amax)
    b.pop(bmin)

print(s)