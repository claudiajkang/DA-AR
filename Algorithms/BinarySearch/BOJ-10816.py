from sys import stdin
read = lambda: stdin.readline().rstrip()

n = int(read())
nc = list(map(int, read().split()))
c = {}

m = int(read())
mc = list(map(int, read().split()))

for i in nc:
    if i not in c.keys():
        c[i] = 0

    c[i] += 1


for j in range(m):
    if mc[j] in c.keys():
        print(c[mc[j]], end = ' ')
    else:
        print(0, end = ' ')

print()
