from sys import stdin

read = lambda: map(int, stdin.readline().rstrip().split())

n, l = read()
broken = list(read())
broken.sort()

idx = 0
res = 1
cur = broken[0]

while idx < n:
    if broken[idx] < (cur + l):
        idx += 1
    else:
        cur = broken[idx]
        res += 1

print(res)
