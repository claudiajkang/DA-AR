from sys import stdin
read = lambda: stdin.readline().rstrip()

n = int(read())
m = int(read())
broken = read().split()

if n == 100:
    print(0)
    exit()

res = abs(n - 100)
for i in range(1000001):
    pos = True
    for j in str(i):
        if j in broken:
            pos = False
            break

    if pos:
        res = min(res, len(str(i))+abs(i-n))

print(res)