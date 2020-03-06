from sys import stdin
read = lambda : stdin.readline().rstrip()

N = int(read())
SC = list(map(int, read().split()))

M = int(read())
TC = list(map(int, read().split()))

R = [str(0)] * M

SC = sorted(SC)

for i in range(M):
    v = TC[i]
    
    lo = 0
    hi = N - 1
    mid = 0

    while lo < hi:
        mid = (lo+hi) // 2

        if SC[mid] < v:
            lo = mid + 1

        else:
            hi = mid

    if SC[hi] == v:
        R[i] = str(1)

print(' '.join(R))
