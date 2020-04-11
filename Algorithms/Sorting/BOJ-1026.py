from sys import stdin

read = lambda: stdin.readline()

n = int(read())
a = list(map(int, read().split()))
b = list(map(int, read().split()))

s = 0
for i in range(n):
    maxA = a.index(max(a))
    minB = b.index(min(b))

    s += (a[maxA] * b[minB])

    a.pop(maxA)
    b.pop(minB)

print(s)
