import sys

T = int(sys.stdin.readline())

for i in range(T):
    N = sys.stdin.readline().split()
    res = int(N[0]) + int(N[1])
    print(res)
