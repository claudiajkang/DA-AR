N = int(input())
A = [int(s) for s in input().split()]
Al = len(A)-1

for i in range(Al, -1, -1):
    if Al != 0:
        print(A[i], end=' ')
    else:
        print(A[i])
