from sys import stdin
read = lambda: stdin.readline()

an, bn = map(int, read().split())
a = set(map(int, read().split()))
b = set(map(int, read().split()))

print(len(a-b)+len(b-a))
