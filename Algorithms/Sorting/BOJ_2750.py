from sys import stdin
read = lambda : int(stdin.readline())

N = read()
PN = [False for _ in range(1000001)]

for i in range(N):
    idx = read()
    PN[idx] = True

c = 0
for i in range(1, 1000001):
    if PN[i]:
        print(i)
        c += 1
        if c == N:
            break

