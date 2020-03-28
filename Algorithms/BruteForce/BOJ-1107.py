from sys import stdin
read = lambda: stdin.readline()

n = int(read())
m = int(read())
broken = read().split()

if n == 100:
    print(0)
    exit()

res = abs(n-100)

for i in range(1000001):
    impossible = False
    for ii in str(i):
        if ii in broken:
            impossible = True
            break

    if not impossible:
        res = min(res, len(str(i))+abs(n-i))

print(res)
