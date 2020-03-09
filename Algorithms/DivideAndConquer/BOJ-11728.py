from sys import stdin
read = lambda: stdin.readline().rstrip()

n, m = map(int, read().split())
l = list(map(int, read().split())) + list(map(int, read().split()))
l.sort()
r = map(str, l)
print(' '.join(r))
