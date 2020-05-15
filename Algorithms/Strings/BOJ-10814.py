from sys import stdin
read = lambda: stdin.readline().rstrip()

n = int(read())
pp = [[] for i in range(n)]

for i in range(n):
    l = read().split()
    pp[i] = [i, int(l[0]), l[1]]

pp.sort(key=lambda x: x[0])
pp.sort(key=lambda x: x[1])

for ii, jj, nn in pp:
    print(f"{jj} {nn}")
