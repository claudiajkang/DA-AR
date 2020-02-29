from sys import stdin
  
M, N = map(int, stdin.readline().split())
PN = [True for _ in range(N+1)]
PN[0], PN[1] = False, False

for i in range(2, N+1):
    if i * i > N:
        break

    if PN[i]:
        for j in range(2, N // i + 1):
            PN[i * j] = False

for i in range(M, N+1):
    if PN[i]:
        print(i)
