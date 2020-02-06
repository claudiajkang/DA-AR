import sys

for i in sys.stdin:
    N = i.split()
    res = int(N[0]) + int(N[1])
    print(res)
