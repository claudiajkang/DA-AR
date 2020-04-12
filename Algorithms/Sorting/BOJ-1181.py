from sys import stdin

read = lambda: stdin.readline().rstrip()

n = int(read())
a = set()

for i in range(n):
    a.add(read())

a = list(a)
a.sort()
a.sort(key=lambda x: len(x))

for i in a:
    print(i)
