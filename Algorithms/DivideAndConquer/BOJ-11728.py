from sys import stdin
read = lambda: stdin.readline().rstrip()

n, m = map(int, read().split())
nmlist = list(map(int, read().split())) + list(map(int, read().split()))
print(' '.join(map(str, sorted(nmlist))))


