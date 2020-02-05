from bisect import bisect

Nn = int(input())
A = list(map(int, input().rstrip().split()))
Mn = int(input())
M = list(map(int, input().rstrip().split()))
A = sorted(A)

for i in M:
    res = bisect(A, i) - 1
    if 0 <= res < Nn and A[res] == i:
        print(1)
    else:
        print(0)