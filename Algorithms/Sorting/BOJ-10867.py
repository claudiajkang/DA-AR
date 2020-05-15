from sys import stdin

read = lambda: stdin.readline().rstrip()

n = int(read())
l = list(map(int, read().split()))
l = list(set(l))

print(" ".join(map(str, sorted(l))))
