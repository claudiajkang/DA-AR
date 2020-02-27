from sys import stdin

M, N = map(int, stdin.readline().split())
PN = [False, False] + [True for _ in range(2, N + 1)]

for i in range(2, N + 1):
    if pow(i, 2) > N:
        break

    if PN[i]:
        v = N // i
        for j in range(2, v + 1):
            PN[i * j] = False

for i in range(M, N + 1):
    if PN[i]:
        print(i)
