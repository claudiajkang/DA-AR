from sys import stdin
read = lambda: stdin.readline().rstrip()

n = int(read())
m = int(read())
broke = read().split()

if n == 100:
    print(0)
    exit()

res = abs(n - 100)

for i in range(1000001):
    e = True
    for j in str(i):
        if j in broke:
            e = False
            break

    if e:
        res = min(res, len(str(i))+abs(i-n))

print(res)