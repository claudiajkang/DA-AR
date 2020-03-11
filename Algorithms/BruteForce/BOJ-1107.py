from sys import stdin
read = lambda: stdin.readline().rstrip()

n = int(read())
m = int(read())
broken = read().split()
channel = []

for i in range(0, 1000001):
    f = True
    for j in broken:
        if j in str(i):
            f = False
            break
    if f:
        channel.append(i)

res = abs(n-100)

for i in channel:
    if abs(i-n) + len(str(i)) < res:
        res = abs(i-n) + len(str(i))

print(res)
