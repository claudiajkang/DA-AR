from sys import stdin
read = lambda : stdin.readline().rstrip()

N = int(read())
v = list(map(int, read().split()))
NC = {}

for i in v:
    if i not in NC.keys():
        NC[i] = 0
    NC[i] += 1

M = int(read())
MC = list(map(int, read().split()))

res = [0] * M

for i in range(M):
    lo = 0
    hi = N
    
    if MC[i] in NC.keys():
        res[i] += NC[MC[i]]

for i in res:
    print(i, end = ' ')

print()
