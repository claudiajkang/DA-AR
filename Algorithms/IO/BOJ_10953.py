import sys

T = int(sys.stdin.readline())

for i in range(T):
    print(sum(map(int, sys.stdin.readline().split(','))))
