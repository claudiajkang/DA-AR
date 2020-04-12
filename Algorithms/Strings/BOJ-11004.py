from sys import stdin

read = lambda: stdin.readline().rstrip()

n, k = map(int, read().split())
l = list(map(int, read().split()))
l.sort()

print(l[k - 1])
