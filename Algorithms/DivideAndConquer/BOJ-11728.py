from sys import stdin
read = lambda: stdin.readline().rstrip()

n, m = map(int, read().split())
a = list(map(int, read().split()))
b = list(map(int, read().split()))

print(' '.join(map(str, sorted(a+b))))
