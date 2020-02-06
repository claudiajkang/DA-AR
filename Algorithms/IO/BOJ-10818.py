import sys

N = int(sys.stdin.readline())
D = list(map(int, sys.stdin.readline().split()))

print(min(D), end=" ")
print(max(D))
