from sys import stdin

read = lambda: map(int, stdin.readline().rstrip().split())

n, l = read()
b = list(read())
b.sort()

res = 1
cur = b[0]

for i in range(n):
    if b[i] < (cur + l): continue
    cur = b[i]
    res += 1

print(res)
