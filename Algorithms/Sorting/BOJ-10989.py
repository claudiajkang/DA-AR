from sys import stdin
read = lambda : int(stdin.readline())

N = read()
PN = [0] * 10001

for i in range(N):
    v = read()
    PN[v] += 1

for i in range(1, 10001):
    if PN[i]:
        for j in range(PN[i]):
            print(i)
