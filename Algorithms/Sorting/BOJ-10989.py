from sys import stdin
read = lambda : int(stdin.readline())

N = read()
PN = [0 for _ in range(10001)]

for i in range(N):
    V = read()
    PN[V] += 1

for i in range(1, 10001):
    if PN[i] > 0:
        for j in range(PN[i]):
            print(i)
