import sys

T = int(sys.stdin.readline())

for i in range(T):
    a, b = map(int, sys.stdin.readline().split())
    pr = "Case #{}: {} + {} = {}".format(str(i+1), str(a), str(b), str(a+b))
    print(pr)
